"""Interactive table display for practice log entries."""

import pandas as pd
import streamlit as st


def display_log_table(sessions: list[dict], show_filters: bool = True):
    """
    Display an interactive table of practice log entries.

    Args:
        sessions: List of practice session dictionaries
        show_filters: Whether to show filter widgets
    """
    if not sessions:
        st.info("No practice sessions recorded yet. Add your first entry!")
        return

    # Convert to DataFrame
    df = pd.DataFrame(sessions)

    # Ensure columns exist
    if "sub_categories" in df.columns:
        df["sub_categories"] = df["sub_categories"].apply(lambda x: ", ".join(x) if x else "")

    # Reorder columns
    column_order = ["date", "notebook", "primary_category", "sub_categories", "completed"]
    existing_cols = [col for col in column_order if col in df.columns]
    df = df[existing_cols]

    # Rename for display
    df = df.rename(
        columns={
            "date": "Date",
            "notebook": "Notebook",
            "primary_category": "Category",
            "sub_categories": "Sub-Categories",
            "completed": "Completed",
        }
    )

    if show_filters:
        st.subheader("Filters")

        col1, col2, col3 = st.columns(3)

        with col1:
            # Date range filter
            if "Date" in df.columns and not df.empty:
                min_date = pd.to_datetime(df["Date"].min())
                max_date = pd.to_datetime(df["Date"].max())

                date_range = st.date_input(
                    "Date Range",
                    value=(min_date, max_date),
                    min_value=min_date,
                    max_value=max_date,
                )

                if len(date_range) == 2:
                    start_date, end_date = date_range
                    df = df[
                        (pd.to_datetime(df["Date"]) >= pd.to_datetime(start_date))
                        & (pd.to_datetime(df["Date"]) <= pd.to_datetime(end_date))
                    ]

        with col2:
            # Category filter
            if "Category" in df.columns:
                categories = df["Category"].unique().tolist()
                selected_categories = st.multiselect(
                    "Categories",
                    options=categories,
                    default=categories,
                )

                if selected_categories:
                    df = df[df["Category"].isin(selected_categories)]

        with col3:
            # Completion filter
            if "Completed" in df.columns:
                completion_filter = st.selectbox(
                    "Completion Status",
                    options=["All", "Completed", "Incomplete"],
                )

                if completion_filter == "Completed":
                    df = df[df["Completed"] == True]
                elif completion_filter == "Incomplete":
                    df = df[df["Completed"] == False]

    # Display the table
    st.subheader(f"Practice Log ({len(df)} entries)")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Date": st.column_config.DateColumn("Date", format="YYYY-MM-DD"),
            "Notebook": st.column_config.TextColumn("Notebook", width="medium"),
            "Category": st.column_config.TextColumn("Category", width="small"),
            "Sub-Categories": st.column_config.TextColumn("Sub-Categories", width="medium"),
            "Completed": st.column_config.CheckboxColumn("Completed", width="small"),
        },
    )

    # Export button
    if not df.empty:
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download as CSV",
            data=csv,
            file_name="practice_log.csv",
            mime="text/csv",
        )


def display_recent_sessions(sessions: list[dict], num_sessions: int = 5):
    """
    Display the most recent practice sessions.

    Args:
        sessions: List of practice session dictionaries (sorted most recent first)
        num_sessions: Number of recent sessions to display
    """
    if not sessions:
        st.info("No practice sessions yet.")
        return

    st.subheader(f"Recent {min(num_sessions, len(sessions))} Sessions")

    recent = sessions[:num_sessions]

    for i, session in enumerate(recent):
        with st.expander(
            f"📅 {session.get('date', 'Unknown')} - {session.get('primary_category', 'Unknown')}"
        ):
            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Notebook:** {session.get('notebook', 'N/A')}")
                st.write(f"**Category:** {session.get('primary_category', 'N/A')}")

            with col2:
                sub_cats = session.get('sub_categories', [])
                st.write(f"**Sub-Categories:** {', '.join(sub_cats) if sub_cats else 'None'}")
                completed = session.get('completed', False)
                status = "✅ Completed" if completed else "⏳ In Progress"
                st.write(f"**Status:** {status}")
