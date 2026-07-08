from __future__ import annotations

import plotly.express as px
import streamlit as st

from source.fast_math.analytics import (
    daily_question_counts_by_type,
    score_distribution,
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

    page = st.session_state._nav_page

    if page == "Dashboard":
        render_dashboard()
    elif page == "New Quiz":
        render_new_quiz()
    else:
        render_take_quiz()


def initialize_state() -> None:
    st.session_state.setdefault("active_quiz", None)
    st.session_state.setdefault("last_feedback", None)
    st.session_state.setdefault("completed_quiz_id", None)
    st.session_state.setdefault("completed_quiz_record", None)
    st.session_state.setdefault("_nav_page", "Dashboard")


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
    activity_chart.update_xaxes(type="category")
    st.plotly_chart(activity_chart, use_container_width=True)

    left, right = st.columns(2)

    dist_df = score_distribution(history)
    dist_chart = px.histogram(
        dist_df,
        x="score_pct",
        title="Quiz Score Distribution (All Topics)",
        range_x=[0, 105],
    )
    dist_chart.update_traces(xbins={"start": 0, "end": 105, "size": 5})
    dist_chart.update_layout(xaxis_title="Score %", yaxis_title="Quizzes")
    left.plotly_chart(dist_chart, use_container_width=True)

    topic_dist_chart = px.histogram(
        dist_df,
        x="score_pct",
        color="topic",
        barmode="overlay",
        opacity=0.7,
        title="Quiz Score Distribution by Topic",
        range_x=[0, 105],
    )
    topic_dist_chart.update_traces(xbins={"start": 0, "end": 105, "size": 5})
    topic_dist_chart.update_layout(xaxis_title="Score %", yaxis_title="Quizzes")
    right.plotly_chart(topic_dist_chart, use_container_width=True)


def render_new_quiz() -> None:
    st.subheader("Start a New Quiz")
    topics = get_topics()
    if not topics:
        st.error("No question generators are available yet.")
        return

    with st.form("new_quiz_form"):
        selected_topics = st.multiselect("Topics", topics, default=topics)
        question_count = st.slider("Number of questions", min_value=1, max_value=25, value=5)
        hints_enabled = st.checkbox("Show hints", value=True)
        use_weights = st.checkbox("Prioritize weak/unseen question types", value=True)
        allow_type_repeats = st.checkbox("Allow repeated question types", value=False)
        submitted = st.form_submit_button("Generate Quiz")

    if submitted:
        if not selected_topics:
            st.warning("Select at least one topic.")
            return
        st.session_state.active_quiz = build_quiz(
            selected_topics=selected_topics,
            question_count=question_count,
            hints_enabled=hints_enabled,
            history=load_quiz_history(),
            use_weights=use_weights,
            allow_type_repeats=allow_type_repeats,
        )
        st.session_state.last_feedback = None
        st.session_state.completed_quiz_id = None
        st.session_state.completed_quiz_record = None
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
    st.caption(
        f"Question {active_quiz.current_index + 1} of {active_quiz.requested_question_count} | Topics: {', '.join(active_quiz.selected_topics)}"
    )
    st.markdown(f"> {question.prompt}")
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
        append_quiz_attempt(record)
        st.session_state.completed_quiz_id = active_quiz.quiz_id
        st.session_state.last_feedback = None
        st.session_state.completed_quiz_record = record
    else:
        record = st.session_state.completed_quiz_record

    st.success(
        f"Quiz complete. Score: {record.correct_count}/{record.correct_count + record.incorrect_count} ({record.score_pct:.1f}%)"
    )
    st.dataframe(
        [
            {
                "topic": question.topic,
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
    if st.button("Clear Active Quiz"):
        st.session_state.active_quiz = None
        st.session_state.completed_quiz_id = None
        st.session_state.completed_quiz_record = None
        st.rerun()
