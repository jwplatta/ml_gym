"""History page showing full practice log with filtering and search."""

import streamlit as st

from dashboard.components.log_table import display_log_table
from dashboard.data.loader import get_all_sessions

st.set_page_config(page_title="History", page_icon="📋", layout="wide")

st.title("📋 Practice History")
st.markdown("View and filter all your practice sessions.")

st.divider()

# Load all sessions
sessions = get_all_sessions()

# Display table with filters
display_log_table(sessions, show_filters=True)

# Optional: Search functionality
if sessions:
    st.divider()
    st.subheader("🔍 Search")

    search_term = st.text_input(
        "Search notebook names",
        placeholder="Type to search...",
    )

    if search_term:
        filtered = [s for s in sessions if search_term.lower() in s.get("notebook", "").lower()]

        if filtered:
            st.write(f"Found {len(filtered)} matching sessions:")
            display_log_table(filtered, show_filters=False)
        else:
            st.info(f"No sessions found matching '{search_term}'")
