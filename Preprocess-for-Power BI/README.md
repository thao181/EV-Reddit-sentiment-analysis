Purpose: Prepare Reddit EV comments dataset for sentiment analysis and interactive Power BI visualization.

Overview

This notebook performs text preprocessing and sentiment labeling on Reddit comments related to Electric Vehicles (EVs).
It automates the process of cleaning, transforming, and exporting structured data that can be directly imported into Power BI for dashboard creation.

Key Steps
# 1. Load Dependencies and Dataset

Libraries used: pandas, nltk, matplotlib.
# 2. Sentiment Classification using VADER

Applied VADER SentimentIntensityAnalyzer from NLTK to each comment.

Generated a compound score (-1 to 1) for each text.

Classified sentiment as:

Positive → compound ≥ 0.05

Negative → compound < 0.05

Neutral → empty or missing comment

# 3. Time-based Feature Extraction

Converted timestamps (post_created_time, comment_created_time) to datetime.

Extracted key temporal fields: year, month, day, hour

These enable Power BI to group and filter data dynamically (e.g., trends over time, sentiment by hour).

# 4. Comment Length Calculation

Computed comment_length_chars — total number of characters per comment — to analyze how sentiment correlates with comment detail.

# 5. Data Cleaning and Export

Removed rows with missing values.

Converted time columns to integers for Power BI compatibility.

Selected only relevant columns:
