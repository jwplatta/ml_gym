"""Overview page with comprehensive statistics and visualizations."""

import streamlit as st

from dashboard.components.calendar_heatmap import create_calendar_heatmap
from dashboard.components.category_chart import (
    create_category_pie_chart,
    create_day_of_week_chart,
)
from dashboard.data.loader import (
    calculate_streak,
    get_all_sessions,
    get_category_breakdown,
    get_session_count_by_date,
)

st.set_page_config(page_title="Overview", page_icon="📊", layout="wide")

st.title("📊 Practice Overview")
st.markdown("Comprehensive view of your practice statistics and patterns.")

st.divider()

# Load data
sessions = get_all_sessions()
session_counts = get_session_count_by_date()
category_breakdown = get_category_breakdown()

# Stats overview
st.subheader("📈 Statistics")

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
st.subheader("📅 Annual Practice Calendar")

if session_counts:
    from datetime import datetime

    current_year = datetime.now().year
    fig = create_calendar_heatmap(session_counts, year=current_year)
    st.pyplot(fig)
else:
    st.info("No practice data yet.")

st.divider()

# Two-column layout for charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Category Distribution")
    if category_breakdown:
        fig = create_category_pie_chart(category_breakdown)
        st.pyplot(fig)
    else:
        st.info("No category data yet.")

with col2:
    st.subheader("📆 Practice by Day of Week")
    if sessions:
        fig = create_day_of_week_chart(sessions)
        st.pyplot(fig)
    else:
        st.info("No practice data yet.")

st.divider()

# Additional insights
if sessions:
    st.subheader("💡 Insights")

    # Most practiced category
    if category_breakdown:
        top_category = max(category_breakdown.items(), key=lambda x: x[1])
        st.write(f"**Most Practiced Category:** {top_category[0]} ({top_category[1]} sessions)")

    # Average sessions per week
    if len(session_counts) > 0:
        avg_per_week = len(sessions) / max(len(session_counts) / 7, 1)
        st.write(f"**Average Sessions Per Week:** {avg_per_week:.1f}")

    # Completion rate
    completed = sum(1 for s in sessions if s.get("completed", False))
    completion_rate = (completed / len(sessions)) * 100 if sessions else 0
    st.write(f"**Completion Rate:** {completion_rate:.1f}%")
