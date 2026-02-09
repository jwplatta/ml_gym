"""GitHub-style calendar heatmap for practice sessions."""

from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from dashboard.config import CALENDAR_COLORS


def create_calendar_heatmap(session_counts: dict[str, int], year: int | None = None):
    """
    Create a GitHub-style calendar heatmap showing practice frequency.

    Args:
        session_counts: Dictionary mapping date strings (YYYY-MM-DD) to session counts
        year: Year to display (defaults to current year)

    Returns:
        matplotlib figure object
    """
    if year is None:
        year = datetime.now().year

    # Create figure
    fig, ax = plt.subplots(figsize=(15, 3))

    # Calculate grid dimensions (53 weeks x 7 days)
    weeks = 53
    days = 7

    # Start from January 1st of the year
    start_date = datetime(year, 1, 1)

    # Find the first Monday (or start of week)
    while start_date.weekday() != 0:  # 0 = Monday
        start_date -= timedelta(days=1)

    # Create grid
    grid = np.zeros((days, weeks))

    # Fill grid with session counts
    for week in range(weeks):
        for day in range(days):
            current_date = start_date + timedelta(weeks=week, days=day)
            if current_date.year != year:
                grid[day, week] = -1  # Mark as outside year
            else:
                date_str = current_date.strftime("%Y-%m-%d")
                grid[day, week] = session_counts.get(date_str, 0)

    # Color mapping function
    def get_color(count):
        if count < 0:
            return "#ffffff"  # White for outside year
        elif count == 0:
            return CALENDAR_COLORS[0]
        elif count < 3:
            return CALENDAR_COLORS[1]
        elif count < 5:
            return CALENDAR_COLORS[3]
        else:
            return CALENDAR_COLORS[5]

    # Draw cells
    cell_size = 1
    for week in range(weeks):
        for day in range(days):
            count = grid[day, week]
            color = get_color(count)

            rect = mpatches.Rectangle(
                (week * cell_size, (days - 1 - day) * cell_size),
                cell_size * 0.95,
                cell_size * 0.95,
                linewidth=1,
                edgecolor="#dddddd",
                facecolor=color,
            )
            ax.add_patch(rect)

    # Add month labels
    month_positions = []
    current_month = start_date.month

    for week in range(weeks):
        current_date = start_date + timedelta(weeks=week)
        if current_date.month != current_month and current_date.year == year:
            month_positions.append((week, current_date.strftime("%b")))
            current_month = current_date.month

    for week, month_label in month_positions:
        ax.text(
            week * cell_size,
            days * cell_size + 0.3,
            month_label,
            fontsize=9,
            va="bottom",
        )

    # Add day labels
    day_labels = ["Mon", "", "Wed", "", "Fri", "", ""]
    for day, label in enumerate(day_labels):
        if label:
            ax.text(
                -0.5,
                (days - 1 - day) * cell_size + cell_size / 2,
                label,
                fontsize=8,
                ha="right",
                va="center",
            )

    # Set axis limits and remove ticks
    ax.set_xlim(-1, weeks * cell_size)
    ax.set_ylim(-0.5, days * cell_size + 1)
    ax.set_aspect("equal")
    ax.axis("off")

    # Add title
    ax.text(
        weeks * cell_size / 2,
        days * cell_size + 1,
        f"Practice Calendar {year}",
        fontsize=12,
        ha="center",
        weight="bold",
    )

    # Add legend
    legend_elements = [
        mpatches.Patch(facecolor=CALENDAR_COLORS[0], edgecolor="#dddddd", label="0"),
        mpatches.Patch(facecolor=CALENDAR_COLORS[1], edgecolor="#dddddd", label="1-2"),
        mpatches.Patch(facecolor=CALENDAR_COLORS[3], edgecolor="#dddddd", label="3-4"),
        mpatches.Patch(facecolor=CALENDAR_COLORS[5], edgecolor="#dddddd", label="5+"),
    ]

    ax.legend(
        handles=legend_elements,
        loc="upper right",
        bbox_to_anchor=(1.02, 1.15),
        ncol=4,
        frameon=False,
        fontsize=8,
        title="Sessions per day",
        title_fontsize=8,
    )

    plt.tight_layout()
    return fig


def create_mini_calendar_heatmap(
    session_counts: dict[str, int], num_weeks: int = 12
):
    """
    Create a mini calendar heatmap showing recent weeks.

    Args:
        session_counts: Dictionary mapping date strings to session counts
        num_weeks: Number of recent weeks to display

    Returns:
        matplotlib figure object
    """
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 2))

    days = 7
    end_date = datetime.now()

    # Find the most recent Sunday
    while end_date.weekday() != 6:  # 6 = Sunday
        end_date -= timedelta(days=1)

    start_date = end_date - timedelta(weeks=num_weeks - 1)

    # Create grid
    grid = np.zeros((days, num_weeks))

    # Fill grid
    for week in range(num_weeks):
        for day in range(days):
            current_date = start_date + timedelta(weeks=week, days=day)
            date_str = current_date.strftime("%Y-%m-%d")
            grid[day, week] = session_counts.get(date_str, 0)

    # Color mapping
    def get_color(count):
        if count == 0:
            return CALENDAR_COLORS[0]
        elif count < 3:
            return CALENDAR_COLORS[1]
        elif count < 5:
            return CALENDAR_COLORS[3]
        else:
            return CALENDAR_COLORS[5]

    # Draw cells
    cell_size = 1
    for week in range(num_weeks):
        for day in range(days):
            count = grid[day, week]
            color = get_color(count)

            rect = mpatches.Rectangle(
                (week * cell_size, (days - 1 - day) * cell_size),
                cell_size * 0.9,
                cell_size * 0.9,
                linewidth=0.5,
                edgecolor="#cccccc",
                facecolor=color,
            )
            ax.add_patch(rect)

    # Add day labels
    day_labels = ["M", "", "W", "", "F", "", ""]
    for day, label in enumerate(day_labels):
        if label:
            ax.text(
                -0.3,
                (days - 1 - day) * cell_size + cell_size / 2,
                label,
                fontsize=7,
                ha="right",
                va="center",
            )

    ax.set_xlim(-0.5, num_weeks * cell_size)
    ax.set_ylim(-0.5, days * cell_size)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    return fig
