"""Main Streamlit application for the ML Gym Practice Dashboard."""

import streamlit as st

from dashboard.components.calendar_heatmap import create_calendar_heatmap
from dashboard.components.log_table import display_recent_sessions
from dashboard.config import INITIAL_SIDEBAR_STATE, LAYOUT, PAGE_ICON, PAGE_TITLE
from dashboard.data.loader import (
    calculate_streak,
    get_all_sessions,
    get_category_breakdown,
    get_session_count_by_date,
)

# Page configuration
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE,
)

# Title
st.title(f"{PAGE_ICON} ML Gym Practice Dashboard")
st.markdown("Track your machine learning practice journey with visualizations and analytics.")

st.divider()

# Load data
sessions = get_all_sessions()
session_counts = get_session_count_by_date()
category_breakdown = get_category_breakdown()

# Quick stats
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Sessions", len(sessions))

with col2:
    unique_dates = len(session_counts)
    st.metric("Days Practiced", unique_dates)

with col3:
    current_streak, longest_streak = calculate_streak()
    st.metric("Current Streak", f"{current_streak} days")

with col4:
    st.metric("Longest Streak", f"{longest_streak} days")

st.divider()

# Calendar heatmap
st.subheader("📅 Practice Calendar")

if session_counts:
    from datetime import datetime

    current_year = datetime.now().year
    fig = create_calendar_heatmap(session_counts, year=current_year)
    st.pyplot(fig)
else:
    st.info("No practice data yet. Add your first session to see the calendar!")

st.divider()

# Recent activity
st.subheader("🕐 Recent Activity")

if sessions:
    display_recent_sessions(sessions, num_sessions=5)
else:
    st.info("No recent practice sessions. Head to the 'Add Entry' page to log your first session!")

# Footer
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: gray; padding: 20px;'>
        <p>ML Gym Practice Dashboard | Track your learning progress</p>
    </div>
    """,
    unsafe_allow_html=True,
)
