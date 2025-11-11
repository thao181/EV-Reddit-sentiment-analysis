Exploratory Data Analysis (EDA)

This notebook explores Reddit comments related to electric vehicles (EVs), focusing on temporal trends, sentiment distribution, and comment characteristics.
The goal is to uncover patterns in public perception over time and across different contexts.

# 1. Sentiment Composition

Calculated the overall share of positive and negative comments.

Result: Positive comments account for the majority, showing a generally optimistic tone toward EVs.

Visualization: Horizontal stacked bar chart highlighting the sentiment proportions.

# 2. Temporal Distribution of Comments
* By Hour of Day

  + Comments peak between 10 AM – 2 PM, indicating higher user activity during midday.

  + Engagement drops sharply overnight (1–5 AM).

* By Month

  + Sharp rises observed in April, August, and December, possibly linked to seasonal discussions or EV-related   policy/news cycles.

  + Visualization: Monthly bar chart showing uneven engagement across the year.

* By Year

  + Steady growth from 2017 to 2025, reflecting increasing public discussion and awareness of EVs.

  + Notable peaks in 2021, 2024, and 2025, coinciding with global EV adoption surges and major policy     announcements.

# 3. Sentiment Divergence by Month

Compared positive vs. negative comment shares per month.

Most months maintain a positive majority, with April–June showing the strongest optimism.

Visualization: Divergent bar chart (positive vs. negative above/below baseline).

# 4. Sentiment by Time of Day

Grouped hours into four time periods:

Morning (5–12h)

Afternoon (12–17h)

Evening (17–22h)

Night (22–5h)

Sentiment remains mostly positive across all time periods, but evening posts show slightly higher negativity, possibly reflecting user fatigue or end-of-day frustration.

# 5. Comment Length vs. Sentiment

Calculated average comment length for each sentiment type.

Positive comments are significantly longer (≈218 chars) than negative ones (≈143 chars).

A t-test (t = 15.79, p < 0.001) confirms the difference is statistically significant.

Interpretation: Positive discussions are more detailed, while negative ones tend to be shorter and more direct.
