from __future__ import annotations

import dataclasses

import plotly.express as px
import streamlit as st

from source.fast_math.analytics import (
    accuracy_by_field,
    daily_question_counts_by_type,
    slowest_question_types,
    summarize_history,
)
from source.fast_math.quiz import ActiveQuiz, build_quiz, finalize_quiz, submit_answer
from source.fast_math.registry import get_topics
from source.fast_math.storage import append_quiz_attempt, load_quiz_history


def run() -> None:
    st.set_page_config(page_title="Fast Math", page_icon="🧠", layout="wide")
    initialize_state()

    st.title("Fast Math")

    with st.sidebar:
        if st.button("Dashboard", use_container_width=True):
            st.session_state._nav_page = "Dashboard"
        if st.button("New Quiz", use_container_width=True):
            st.session_state._nav_page = "New Quiz"
        if st.button("Quiz", use_container_width=True):
            st.session_state._nav_page = "Quiz"
        if st.button("History", use_container_width=True):
            st.session_state._nav_page = "History"
            st.session_state._history_quiz_id = None

    page = st.session_state._nav_page

    if page == "Dashboard":
        render_dashboard()
    elif page == "New Quiz":
        render_new_quiz()
    elif page == "History":
        render_history()
    else:
        render_take_quiz()


def initialize_state() -> None:
    st.session_state.setdefault("active_quiz", None)
    st.session_state.setdefault("last_feedback", None)
    st.session_state.setdefault("completed_quiz_id", None)
    st.session_state.setdefault("completed_quiz_record", None)
    st.session_state.setdefault("confidence_ratings", {})
    st.session_state.setdefault("quiz_saved", False)
    st.session_state.setdefault("_nav_page", "Dashboard")
    st.session_state.setdefault("_history_quiz_id", None)


def render_dashboard() -> None:
    history = load_quiz_history()
    summary = summarize_history(history)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Quizzes", summary["quizzes_completed"])
    col2.metric("Questions", summary["questions_answered"])
    col3.metric("Accuracy", f"{summary['accuracy_pct']:.1f}%")
    col4.metric("Practice Days", summary["practice_days"])

    if not history:
        st.info("No quiz history yet. Start a quiz to populate the dashboard.")
        return

    st.subheader("Practice Activity")
    daily_df = daily_question_counts_by_type(history)
    all_dates = sorted(daily_df["date"].unique())
    if len(all_dates) > 1:
        min_date, max_date = all_dates[0], all_dates[-1]
        default_start = all_dates[-10] if len(all_dates) >= 10 else min_date
        date_range = st.select_slider(
            "Date range",
            options=all_dates,
            value=(default_start, max_date),
            label_visibility="collapsed",
            key=f"activity_date_range_{min_date}_{max_date}",
        )
        daily_df = daily_df[daily_df["date"].between(date_range[0], date_range[1])].sort_values("date")
    activity_chart = px.bar(
        daily_df,
        x="date",
        y="questions_completed",
        color="topic",
        title="Questions Answered Per Day",
    )
    activity_chart.update_layout(
        xaxis_title="Date",
        yaxis_title="Questions Answered",
        barmode="stack",
        margin={"l": 20, "r": 20, "t": 40, "b": 20},
    )
    activity_chart.update_xaxes(type="category", categoryorder="category ascending")
    st.plotly_chart(activity_chart, use_container_width=True)

    topic_acc_df = accuracy_by_field(history, "topic")
    topic_acc_chart = px.bar(
        topic_acc_df,
        x="topic",
        y="accuracy_pct",
        text="questions_answered",
        title="Accuracy by Topic",
    )
    topic_acc_chart.update_layout(xaxis_title="Topic", yaxis_title="Accuracy %", yaxis_range=[0, 100])
    st.plotly_chart(topic_acc_chart, use_container_width=True)

    slow_df = slowest_question_types(history, n=10)
    if not slow_df.empty:
        slow_chart = px.bar(
            slow_df,
            x="question_type",
            y="avg_seconds",
            text="count",
            title="Slowest Question Types (Avg Response Time)",
        )
        slow_chart.update_traces(texttemplate="n=%{text}", textposition="outside")
        max_val = slow_df["avg_seconds"].max()
        slow_chart.update_layout(
            xaxis_title="Question Type",
            yaxis_title="Avg Seconds",
            yaxis_range=[0, max_val * 1.2],
            xaxis_tickangle=45,
        )
        st.plotly_chart(slow_chart, use_container_width=True)


def render_new_quiz() -> None:
    st.subheader("Start a New Quiz")
    topics = get_topics()
    if not topics:
        st.error("No question generators are available yet.")
        return

    with st.form("new_quiz_form"):
        selected_topics = st.multiselect("Topics", topics, default=topics)
        question_count = st.slider("Number of questions", min_value=1, max_value=25, value=5)

        st.markdown("**Effort distribution** (must sum to 100)")
        dist_cols = st.columns(3)
        pct_low = dist_cols[0].number_input("% Low", min_value=0, max_value=100, value=40, step=5)
        pct_medium = dist_cols[1].number_input("% Medium", min_value=0, max_value=100, value=40, step=5)
        pct_high = dist_cols[2].number_input("% High", min_value=0, max_value=100, value=20, step=5)

        hints_enabled = st.checkbox("Show hints", value=True)
        use_weights = st.checkbox("Prioritize weak/unseen question types", value=True)
        allow_type_repeats = st.checkbox("Allow repeated question types", value=False)
        submitted = st.form_submit_button("Generate Quiz")

    if submitted:
        if not selected_topics:
            st.warning("Select at least one topic.")
            return
        total_pct = pct_low + pct_medium + pct_high
        if total_pct != 100:
            st.error(f"Effort distribution must sum to 100% (currently {total_pct}%).")
            return
        effort_distribution = {
            "low": pct_low / 100,
            "medium": pct_medium / 100,
            "high": pct_high / 100,
        }
        # Exclude effort levels set to 0%
        selected_efforts = [level for level, pct in [("low", pct_low), ("medium", pct_medium), ("high", pct_high)] if pct > 0]
        st.session_state.active_quiz = build_quiz(
            selected_topics=selected_topics,
            question_count=question_count,
            hints_enabled=hints_enabled,
            history=load_quiz_history(),
            use_weights=use_weights,
            allow_type_repeats=allow_type_repeats,
            selected_efforts=selected_efforts,
            effort_distribution=effort_distribution,
        )
        st.session_state.last_feedback = None
        st.session_state.completed_quiz_id = None
        st.session_state.completed_quiz_record = None
        st.session_state.confidence_ratings = {}
        st.session_state.quiz_saved = False
        st.session_state._nav_page = "Quiz"
        st.rerun()


def render_take_quiz() -> None:
    st.subheader("Take Quiz")
    active_quiz: ActiveQuiz | None = st.session_state.active_quiz
    if active_quiz is None:
        st.info("No active quiz. Generate one from the New Quiz page.")
        return

    if active_quiz.completed:
        render_completed_quiz(active_quiz)
        return

    question = active_quiz.current_question
    _effort_colors = {"low": "#2e7d32", "medium": "#e65100", "high": "#b71c1c"}
    effort_color = _effort_colors.get(question.effort, "#666")
    st.caption(
        f"Question {active_quiz.current_index + 1} of {active_quiz.requested_question_count} | Topics: {', '.join(active_quiz.selected_topics)}"
    )
    st.markdown(f"> {question.prompt}")
    st.markdown(
        f"<span style='color:{effort_color}; font-size:0.75rem; font-weight:600'>● {question.effort} effort</span>",
        unsafe_allow_html=True,
    )
    if active_quiz.hints_enabled and question.hint:
        st.info(question.hint)

    with st.form(f"question_form_{question.question_id}", clear_on_submit=True):
        answer = st.text_input("Your answer")
        submitted = st.form_submit_button("Submit")

    if submitted:
        attempt = submit_answer(active_quiz, answer)
        st.session_state.last_feedback = {
            "question_id": attempt.question_id,
            "is_correct": attempt.is_correct,
            "answer_display": attempt.answer_display,
        }
        st.rerun()


def render_completed_quiz(active_quiz: ActiveQuiz) -> None:
    if st.session_state.completed_quiz_id != active_quiz.quiz_id:
        record = finalize_quiz(active_quiz)
        st.session_state.completed_quiz_id = active_quiz.quiz_id
        st.session_state.last_feedback = None
        st.session_state.completed_quiz_record = record
        st.session_state.confidence_ratings = {}
        st.session_state.quiz_saved = False
    else:
        record = st.session_state.completed_quiz_record

    st.success(
        f"Quiz complete. Score: {record.correct_count}/{record.correct_count + record.incorrect_count} ({record.score_pct:.1f}%)"
    )
    st.dataframe(
        [
            {
                "topic": question.topic,
                "effort": question.effort,
                "question_type": question.question_type,
                "prompt": question.prompt,
                "your_answer": question.raw_user_answer,
                "correct_answer": question.answer_display,
                "correct": question.is_correct,
            }
            for question in record.questions
        ],
        use_container_width=True,
        hide_index=True,
    )

    # Confidence rating UI
    st.subheader("Rate your confidence")
    st.caption("1 = guessed / no idea  ·  5 = solid, could explain it")
    ratings = st.session_state.confidence_ratings
    for question in record.questions:
        cols = st.columns([4, 1, 1, 1, 1, 1])
        cols[0].markdown(
            f"<small><b>{question.question_type}</b><br>{question.prompt[:80]}{'…' if len(question.prompt) > 80 else ''}</small>",
            unsafe_allow_html=True,
        )
        current = ratings.get(question.question_id)
        for i, col in enumerate(cols[1:], start=1):
            label = f"{'★' if current == i else str(i)}"
            if col.button(label, key=f"conf_{question.question_id}_{i}"):
                st.session_state.confidence_ratings[question.question_id] = i
                st.rerun()

    st.divider()
    if not st.session_state.quiz_saved:
        save_label = "Save Quiz & Ratings" if ratings else "Save Quiz"
        if st.button(save_label, type="primary"):
            updated_questions = [
                dataclasses.replace(
                    q, confidence=ratings.get(q.question_id)
                )
                for q in record.questions
            ]
            updated_record = dataclasses.replace(record, questions=updated_questions)
            append_quiz_attempt(updated_record)
            st.session_state.quiz_saved = True
            st.rerun()
    else:
        st.success("Quiz saved.")

    if st.button("Clear Active Quiz"):
        st.session_state.active_quiz = None
        st.session_state.completed_quiz_id = None
        st.session_state.completed_quiz_record = None
        st.session_state.confidence_ratings = {}
        st.session_state.quiz_saved = False
        st.rerun()


def render_history() -> None:
    history = load_quiz_history()

    selected_id = st.session_state._history_quiz_id

    if selected_id is not None:
        # Find the most recent saved record for this quiz_id (last one wins for re-saves)
        record = next(
            (q for q in reversed(history) if q["quiz_id"] == selected_id), None
        )
        if record is None:
            st.error("Quiz not found.")
            st.session_state._history_quiz_id = None
            st.rerun()
            return
        _render_history_detail(record)
        return

    # --- List view ---
    st.subheader("Quiz History")

    if not history:
        st.info("No quiz history yet. Complete a quiz to see it here.")
        return

    # Deduplicate: keep last record per quiz_id (re-saved quizzes appear multiple times)
    seen: set[str] = set()
    unique: list[dict] = []
    for q in reversed(history):
        if q["quiz_id"] not in seen:
            seen.add(q["quiz_id"])
            unique.append(q)
    unique.reverse()  # restore chronological order, oldest first

    for record in reversed(unique):  # show newest first
        topics = sorted({q["topic"] for q in record.get("questions", [])})
        completed_at = record.get("completed_at", "")[:16].replace("T", " ")
        score = record.get("score_pct", 0.0)
        n_questions = len(record.get("questions", []))
        col_date, col_topics, col_score, col_link = st.columns([2, 3, 1, 1])
        col_date.write(completed_at)
        col_topics.write(", ".join(topics))
        col_score.write(f"{score:.1f}%")
        if col_link.button("View", key=f"view_{record['quiz_id']}"):
            st.session_state._history_quiz_id = record["quiz_id"]
            st.rerun()


def _render_history_detail(record: dict) -> None:
    if st.button("← Back to History"):
        st.session_state._history_quiz_id = None
        st.rerun()

    completed_at = record.get("completed_at", "")[:16].replace("T", " ")
    topics = sorted({q["topic"] for q in record.get("questions", [])})
    st.subheader(f"Quiz — {completed_at}")
    st.caption(f"Topics: {', '.join(topics)}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Score", f"{record.get('score_pct', 0):.1f}%")
    col2.metric("Correct", record.get("correct_count", 0))
    col3.metric("Incorrect", record.get("incorrect_count", 0))

    questions = record.get("questions", [])
    st.dataframe(
        [
            {
                "topic": q.get("topic", ""),
                "effort": q.get("effort", ""),
                "question_type": q.get("question_type", ""),
                "prompt": q.get("prompt", ""),
                "your_answer": q.get("raw_user_answer", ""),
                "correct_answer": q.get("answer_display", ""),
                "correct": q.get("is_correct", False),
                "confidence": q.get("confidence"),
                "time (s)": q.get("response_time_seconds", ""),
            }
            for q in questions
        ],
        use_container_width=True,
        hide_index=True,
    )
