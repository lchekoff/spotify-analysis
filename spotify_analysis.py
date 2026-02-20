#SPOTIFY TOP 200 KAGGLE ANALYSIS

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
df=pd.read_csv("Spotify_Dataset_V3.csv", sep=";", engine="python")
#look at column names
print(df.columns)
#remove missing values
df=df.dropna()

#TOP ARTISTS
#top 200 dataset uses "Artist"
top_artists=df["Artists"].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_artists.values, y=top_artists.index)
plt.title("Top 10 Artists")
plt.xlabel("Number of Songs in Top 200")
plt.show()

#MOST POPULAR TRACKS
#top songs by streams
top_tracks = df.sort_values("Points (Total)", ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_tracks["Points (Total)"], y=top_tracks["Title"])
plt.title("Top 10 Most Streamed Songs")
plt.show()

#STREAMS BY ARTIST
points_by_artist = df.groupby("Artists")["Points (Total)"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=points_by_artist.values, y=points_by_artist.index)
plt.title("Artists with Most Total Points")
plt.xlabel("Total Spotify Chart Points")
plt.ticklabel_format(style='plain', axis='x')
plt.show()
