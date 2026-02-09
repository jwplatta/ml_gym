"""Configuration file for the practice dashboard."""

from pathlib import Path

# File paths
PROJECT_ROOT = Path(__file__).parent.parent
PRACTICE_LOG_PATH = PROJECT_ROOT / "practice_log.json"
LOCK_TIMEOUT = 5.0  # seconds

# Calendar heatmap color scheme (GitHub-style)
CALENDAR_COLORS = {
    0: "#ebedf0",  # No practice (light gray)
    1: "#c6e48b",  # 1-2 sessions (light green)
    3: "#7bc96f",  # 3-4 sessions (medium green)
    5: "#239a3b",  # 5+ sessions (dark green)
}

# Default practice categories
DEFAULT_CATEGORIES = [
    "probability",
    "statistics",
    "machine_learning",
    "deep_learning",
    "pandas",
    "numpy",
    "linear_algebra",
    "algorithms",
    "finance",
    "python",
]

# Streamlit page configuration
PAGE_TITLE = "ML Gym Practice Dashboard"
PAGE_ICON = "📊"
LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# Visualization settings
CHART_HEIGHT = 400
CALENDAR_HEIGHT = 200
TABLE_HEIGHT = 500
