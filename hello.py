from preswald import text, plotly, connect, get_df, table, slider
import pandas as pd
import plotly.express as px

# Custom Text for Branding
text("# 🎧 Spotify Hype")
text("Explore the top songs on Spotify based on various attributes like energy, danceability, and more.")

# Load the CSV (adjust if the dataset is named differently in the config)
connect()
df = get_df("popular_spotify_songs")  # Match to the dataset name in your config

# Slider to dynamically filter based on Energy %
energy_threshold = slider("Minimum Energy (%)", min_val=0, max_val=100, default=50)

# Filter the dataset based on the energy threshold selected
filtered_df = df[df["energy_%"] >= energy_threshold]

# Show the filtered data in a table
table(filtered_df[["track_name", "artist(s)_name", "energy_%", "danceability_%", "valence_%"]],
      title=f"Songs with Energy >= {energy_threshold}%")

# Create a Scatter Plot showing Danceability vs Energy
fig = px.scatter(filtered_df, x="danceability_%", y="energy_%", color="valence_%",
                 hover_data=["track_name", "artist(s)_name"],
                 title="Danceability vs. Energy",
                 labels={"danceability_%": "Danceability (%)", "energy_%": "Energy (%)"})

# Add labels for each point
fig.update_traces(textposition="top center", marker=dict(size=12))

# Customize the appearance of the plot
fig.update_layout(template="plotly_white", title_font=dict(size=20), hoverlabel=dict(bgcolor="white"))

# Display the plot
plotly(fig)

