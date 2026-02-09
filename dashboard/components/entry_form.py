"""Form component for adding new practice log entries."""

from datetime import date

import streamlit as st

from dashboard.config import DEFAULT_CATEGORIES
from dashboard.data.loader import get_all_categories, get_all_sub_categories
from dashboard.data.writer import add_practice_entry


def render_entry_form():
    """Render the form for adding a new practice entry."""
    st.subheader("Add New Practice Entry")

    with st.form("practice_entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            # Date input
            entry_date = st.date_input(
                "Practice Date",
                value=date.today(),
                max_value=date.today(),
                help="Select the date of your practice session",
            )

            # Notebook path
            notebook = st.text_input(
                "Notebook Path",
                placeholder="notebooks/practice/probability_bayes_01_01_2026.ipynb",
                help="Relative path to the practice notebook",
            )

        with col2:
            # Primary category
            existing_categories = list(get_all_categories())
            all_categories = sorted(set(DEFAULT_CATEGORIES + existing_categories))

            primary_category = st.selectbox(
                "Primary Category",
                options=all_categories + ["Other"],
                help="Main category of practice",
            )

            # If "Other" is selected, show text input
            if primary_category == "Other":
                primary_category = st.text_input(
                    "Enter Custom Category",
                    placeholder="e.g., reinforcement_learning",
                )

        # Sub-categories
        existing_sub_cats = list(get_all_sub_categories())
        sub_categories = st.multiselect(
            "Sub-Categories",
            options=sorted(existing_sub_cats) if existing_sub_cats else [],
            help="Select or type sub-categories (e.g., bayes, conditional_probability)",
        )

        # Option to add custom sub-category
        custom_sub_cat = st.text_input(
            "Add Custom Sub-Category (optional)",
            placeholder="Type and press Enter",
        )

        if custom_sub_cat and custom_sub_cat not in sub_categories:
            sub_categories.append(custom_sub_cat)

        # Completion status
        completed = st.checkbox("Mark as Completed", value=True)

        # Submit button
        submit_button = st.form_submit_button("Add Practice Entry", use_container_width=True)

        if submit_button:
            # Validate inputs
            if not notebook.strip():
                st.error("Please enter a notebook path")
            elif not primary_category or primary_category == "Other":
                st.error("Please select or enter a primary category")
            else:
                # Add entry
                date_str = entry_date.strftime("%Y-%m-%d")

                success, message = add_practice_entry(
                    notebook=notebook.strip(),
                    primary_category=primary_category.strip(),
                    sub_categories=sub_categories,
                    completed=completed,
                    date=date_str,
                )

                if success:
                    st.success(message)
                    st.balloons()
                    # Force page rerun to show updated data
                    st.rerun()
                else:
                    st.error(message)


def render_quick_add_form():
    """Render a compact quick-add form."""
    st.subheader("Quick Add")

    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        notebook = st.text_input(
            "Notebook",
            placeholder="notebooks/practice/...",
            key="quick_notebook",
            label_visibility="collapsed",
        )

    with col2:
        existing_categories = list(get_all_categories())
        all_categories = sorted(set(DEFAULT_CATEGORIES + existing_categories))

        category = st.selectbox(
            "Category",
            options=all_categories,
            key="quick_category",
            label_visibility="collapsed",
        )

    with col3:
        if st.button("Add", use_container_width=True, type="primary"):
            if notebook.strip() and category:
                date_str = date.today().strftime("%Y-%m-%d")

                success, message = add_practice_entry(
                    notebook=notebook.strip(),
                    primary_category=category,
                    sub_categories=[],
                    completed=True,
                    date=date_str,
                )

                if success:
                    st.success("✓ Added")
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.warning("Fill in all fields")
