# Spotify Top 200 Kaggle Analysis

This project analyzes the Spotify Top 200 dataset to identify popular artists and songs using Python data analysis and visualization tools.

## Project Overview

The script:

- Loads and cleans Spotify chart data
- Identifies the top 10 artists by number of chart appearances
- Finds the top 10 most streamed songs
- Calculates which artists have the highest total chart points
- Displays results using bar charts

## Dataset

File used: Spotify_Dataset_V3.csv  
Format: semicolon-separated values

The dataset includes artist names, song titles, and total Spotify chart points.

## Technologies Used

Python  
pandas  
matplotlib  
seaborn  

## How to Run

1. Install required libraries:

pip install pandas matplotlib seaborn

2. Place the dataset file in the same folder as the script.

3. Run the program:

python spotify_analysis.py

## Output

The program generates three visualizations:

- Top 10 Artists — artists appearing most frequently in the Top 200
- Top 10 Most Streamed Songs — songs with the highest total chart points
- Artists with Most Total Points — artists with the greatest cumulative chart performance

## Data Cleaning

Missing values are removed to ensure accurate results.

## Notes

The dataset uses the column "Artists" for artist names.  
Popularity is measured using "Points (Total)".

## License

This project is open source and free to use.
