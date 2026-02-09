# ML Gym Practice Dashboard

A Streamlit-based dashboard for tracking and visualizing your machine learning practice sessions.

## Features

- **📅 Calendar Heatmap**: GitHub-style contribution calendar showing practice frequency
- **📊 Analytics**: Detailed charts and statistics about your practice patterns
- **➕ Add Entries**: Form to log new practice sessions
- **📋 History**: Full table view with filtering and search
- **🔒 Safe Writes**: Atomic file operations with locking to prevent data corruption

## Running the Dashboard

### Option 1: Using the Launcher Script (Recommended)

From the ml_gym root directory:

```bash
# Using the shell script
./bin/dashboard

# Or using the Python script
python bin/dashboard.py
# or
./bin/dashboard.py
```

### Option 2: Direct Streamlit Command

```bash
streamlit run dashboard/app.py
```

The dashboard will open in your browser at `http://localhost:8501`

## Structure

```
dashboard/
├── app.py                         # Main entry point
├── config.py                      # Configuration settings
├── data/
│   ├── loader.py                  # Data loading with caching
│   ├── writer.py                  # Atomic writes with file locking
│   └── validator.py               # Data validation
├── components/
│   ├── calendar_heatmap.py        # GitHub-style calendar
│   ├── category_chart.py          # Bar charts and visualizations
│   ├── log_table.py               # Interactive table display
│   └── entry_form.py              # Add entry form
└── pages/
    ├── 1_📊_Overview.py           # Main dashboard
    ├── 2_➕_Add_Entry.py           # Add new entries
    ├── 3_📈_Analytics.py          # Detailed analytics
    └── 4_📋_History.py            # Full log table
```

## Features by Page

### Home (app.py)
- Quick stats: Total sessions, days practiced, current streak, longest streak
- Annual calendar heatmap
- 5 most recent practice sessions

### 📊 Overview
- Comprehensive statistics
- Annual calendar
- Category distribution pie chart
- Practice by day of week
- Key insights

### ➕ Add Entry
- Form to add new practice sessions
- Fields: Date, notebook path, category, sub-categories, completion status
- Recently added entries

### 📈 Analytics
- Cumulative sessions over time (line chart)
- Sessions by category (bar chart)
- Practice by day of week
- Sub-category breakdown
- Detailed statistics

### 📋 History
- Full table of all practice sessions
- Filters: Date range, categories, completion status
- Search by notebook name
- Export to CSV

## Data Storage

Practice sessions are stored in `practice_log.json` at the root of the ml_gym repository.

### Format

```json
{
  "2026-02-08": [
    {
      "notebook": "notebooks/practice/probability_bayes.ipynb",
      "primary_category": "probability",
      "sub_categories": ["bayes", "conditional_probability"],
      "completed": true,
      "date": "2026-02-08"
    }
  ]
}
```

## Dependencies

All required dependencies are in `pyproject.toml`:
- streamlit
- filelock
- matplotlib
- seaborn
- pandas
- numpy

## Tips

- **Adding Entries**: Use the sidebar to navigate to "Add Entry"
- **Filtering**: Use the History page for advanced filtering and search
- **Categories**: Categories are automatically populated from existing entries
- **Concurrent Access**: File locking prevents corruption when multiple users add entries

## Development

The dashboard uses:
- **Streamlit caching**: Data is cached for performance
- **File locking**: Atomic writes prevent concurrent write issues
- **Validation**: All entries are validated before being saved
- **Error handling**: Graceful handling of missing files and corrupted data
