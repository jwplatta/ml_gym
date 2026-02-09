"""Page for adding new practice log entries."""

import streamlit as st

from dashboard.components.entry_form import render_entry_form
from dashboard.components.log_table import display_recent_sessions
from dashboard.data.loader import get_all_sessions

st.set_page_config(page_title="Add Entry", page_icon="➕", layout="wide")

st.title("➕ Add Practice Entry")
st.markdown("Log a new practice session to track your progress.")

st.divider()

# Render the entry form
render_entry_form()

st.divider()

# Show recent entries for reference
st.subheader("📋 Recently Added Entries")

sessions = get_all_sessions()

if sessions:
    display_recent_sessions(sessions, num_sessions=3)
else:
    st.info("No entries yet. Your first entry will appear here!")
