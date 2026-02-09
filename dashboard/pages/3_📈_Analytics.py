"""Analytics page with detailed trends and statistics."""

import streamlit as st

from dashboard.components.category_chart import (
    create_category_bar_chart,
    create_day_of_week_chart,
    create_time_series_chart,
)
from dashboard.data.loader import (
    get_all_sessions,
    get_category_breakdown,
    get_sub_category_breakdown,
)

st.set_page_config(page_title="Analytics", page_icon="📈", layout="wide")

st.title("📈 Practice Analytics")
st.markdown("Detailed analysis of your practice patterns and trends.")

st.divider()

# Load data
sessions = get_all_sessions()
category_breakdown = get_category_breakdown()
sub_category_breakdown = get_sub_category_breakdown()

# Time series
st.subheader("📊 Practice Progress Over Time")

if sessions:
    fig = create_time_series_chart(sessions)
    st.pyplot(fig)
else:
    st.info("No practice data yet.")

st.divider()

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Sessions by Category")
    if category_breakdown:
        fig = create_category_bar_chart(category_breakdown)
        st.pyplot(fig)
    else:
        st.info("No category data yet.")

with col2:
    st.subheader("📅 Practice by Day of Week")
    if sessions:
        fig = create_day_of_week_chart(sessions)
        st.pyplot(fig)
    else:
        st.info("No practice data yet.")

st.divider()

# Sub-category breakdown
st.subheader("🔖 Sub-Category Breakdown")

if sub_category_breakdown:
    fig = create_category_bar_chart(sub_category_breakdown)
    st.pyplot(fig)
else:
    st.info("No sub-category data yet.")

st.divider()

# Detailed statistics
if sessions:
    st.subheader("📊 Detailed Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Categories", len(category_breakdown))

    with col2:
        st.metric("Total Sub-Categories", len(sub_category_breakdown))

    with col3:
        completed = sum(1 for s in sessions if s.get("completed", False))
        st.metric("Completed Sessions", completed)

    # Most common sub-categories
    if sub_category_breakdown:
        st.write("**Top 5 Sub-Categories:**")
        top_sub_cats = sorted(sub_category_breakdown.items(), key=lambda x: x[1], reverse=True)[:5]

        for sub_cat, count in top_sub_cats:
            st.write(f"- {sub_cat}: {count} sessions")
