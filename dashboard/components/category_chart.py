"""Charts for visualizing practice sessions by category."""

import matplotlib.pyplot as plt
import seaborn as sns


def create_category_bar_chart(category_breakdown: dict[str, int]):
    """
    Create a horizontal bar chart of practice sessions by category.

    Args:
        category_breakdown: Dictionary mapping categories to session counts

    Returns:
        matplotlib figure object
    """
    if not category_breakdown:
        # Return empty figure with message
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.text(
            0.5,
            0.5,
            "No practice data yet",
            ha="center",
            va="center",
            fontsize=14,
            color="gray",
        )
        ax.axis("off")
        return fig

    # Sort by count descending
    sorted_items = sorted(category_breakdown.items(), key=lambda x: x[1], reverse=True)
    categories = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]

    # Create figure
    fig, ax = plt.subplots(figsize=(10, max(4, len(categories) * 0.4)))

    # Create horizontal bar chart
    sns.set_style("whitegrid")
    colors = sns.color_palette("husl", len(categories))

    bars = ax.barh(categories, counts, color=colors, edgecolor="black", linewidth=0.5)

    # Add value labels on bars
    for i, (bar, count) in enumerate(zip(bars, counts)):
        ax.text(
            count + max(counts) * 0.02,
            bar.get_y() + bar.get_height() / 2,
            str(count),
            va="center",
            fontsize=10,
            weight="bold",
        )

    ax.set_xlabel("Number of Sessions", fontsize=11, weight="bold")
    ax.set_ylabel("Category", fontsize=11, weight="bold")
    ax.set_title("Practice Sessions by Category", fontsize=13, weight="bold", pad=15)

    # Remove top and right spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    return fig


def create_category_pie_chart(category_breakdown: dict[str, int]):
    """
    Create a pie chart of practice sessions by category.

    Args:
        category_breakdown: Dictionary mapping categories to session counts

    Returns:
        matplotlib figure object
    """
    if not category_breakdown:
        # Return empty figure with message
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.text(
            0.5,
            0.5,
            "No practice data yet",
            ha="center",
            va="center",
            fontsize=14,
            color="gray",
        )
        ax.axis("off")
        return fig

    # Sort by count descending
    sorted_items = sorted(category_breakdown.items(), key=lambda x: x[1], reverse=True)
    categories = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]

    # Create figure
    fig, ax = plt.subplots(figsize=(8, 6))

    colors = sns.color_palette("husl", len(categories))

    wedges, texts, autotexts = ax.pie(
        counts,
        labels=categories,
        colors=colors,
        autopct="%1.1f%%",
        startangle=90,
        textprops={"fontsize": 10},
    )

    # Make percentage text bold
    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontweight("bold")

    ax.set_title(
        "Category Distribution", fontsize=14, weight="bold", pad=20
    )

    plt.tight_layout()
    return fig


def create_time_series_chart(sessions: list[dict]):
    """
    Create a time series line chart of cumulative sessions over time.

    Args:
        sessions: List of practice session dictionaries

    Returns:
        matplotlib figure object
    """
    if not sessions:
        # Return empty figure with message
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.text(
            0.5,
            0.5,
            "No practice data yet",
            ha="center",
            va="center",
            fontsize=14,
            color="gray",
        )
        ax.axis("off")
        return fig

    # Group by date and count
    from collections import defaultdict
    from datetime import datetime

    date_counts = defaultdict(int)
    for session in sessions:
        date_counts[session["date"]] += 1

    # Sort dates
    sorted_dates = sorted(date_counts.keys())

    # Create cumulative counts
    cumulative = []
    total = 0
    for date in sorted_dates:
        total += date_counts[date]
        cumulative.append(total)

    # Convert dates to datetime objects
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in sorted_dates]

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(dates, cumulative, linewidth=2.5, color="#2E86AB", marker="o", markersize=4)

    ax.set_xlabel("Date", fontsize=11, weight="bold")
    ax.set_ylabel("Cumulative Sessions", fontsize=11, weight="bold")
    ax.set_title(
        "Practice Progress Over Time", fontsize=13, weight="bold", pad=15
    )

    ax.grid(True, alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Rotate date labels
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    return fig


def create_day_of_week_chart(sessions: list[dict]):
    """
    Create a bar chart showing practice sessions by day of week.

    Args:
        sessions: List of practice session dictionaries

    Returns:
        matplotlib figure object
    """
    if not sessions:
        # Return empty figure with message
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(
            0.5,
            0.5,
            "No practice data yet",
            ha="center",
            va="center",
            fontsize=14,
            color="gray",
        )
        ax.axis("off")
        return fig

    from collections import defaultdict
    from datetime import datetime

    # Count sessions by day of week
    day_counts = defaultdict(int)
    for session in sessions:
        date = datetime.strptime(session["date"], "%Y-%m-%d")
        day_name = date.strftime("%A")
        day_counts[day_name] += 1

    # Order days properly
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days = [day for day in day_order if day in day_counts]
    counts = [day_counts[day] for day in days]

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 5))

    colors = sns.color_palette("coolwarm", len(days))
    bars = ax.bar(days, counts, color=colors, edgecolor="black", linewidth=0.5)

    # Add value labels on bars
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + max(counts) * 0.02,
            str(int(count)),
            ha="center",
            va="bottom",
            fontsize=10,
            weight="bold",
        )

    ax.set_xlabel("Day of Week", fontsize=11, weight="bold")
    ax.set_ylabel("Number of Sessions", fontsize=11, weight="bold")
    ax.set_title("Practice Sessions by Day of Week", fontsize=13, weight="bold", pad=15)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    return fig
