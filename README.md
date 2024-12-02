# Spotify User Data Extraction and Song Recommender

This repository contains two projects focused on interacting with Spotify's API to extract user data and implement a song recommendation system.

## Table of Contents
1. [Project Descriptions](#Project-Descriptions)
- 1. [User Data Extraction](#User-Data-Extraction)
- 2. [Song Recommender](#Song-Recommender)
2. [Technologies Used](#Technologies-Used)
3. [Getting Started](#Getting-Started)
4. [Setup](#Setup)
5. [Running the Projects](#Running-the-Projects)



## Project Descriptions
1. User Data Extraction
This Python script uses the Spotify Web API to extract user playlist data, including track details, artist information, and audio features.

#### Features:

- Retrieves playlists of the authenticated user.
- Extracts detailed track information, such as:
- Track name, artist, album, and popularity.
- Artist details, including genres and popularity.
- Audio features like danceability, energy, tempo, and more.
- Outputs the data into a structured CSV file for further analysis.
#### File: User Data Extraction.py


2. Song Recommender
This Jupyter Notebook builds a song recommendation system using Spotify's audio features. By analyzing the characteristics of songs, it recommends similar tracks that align with the user’s preferences.

#### Features:

- Loads Spotify track data for analysis.
- Applies similarity-based recommendation logic using features like tempo, danceability, and energy.
- Includes data visualization for understanding patterns in song attributes.
#### File: Song Recommender.ipynb

## Technologies Used

Python Libraries:
- spotipy for Spotify API interaction.
- -pandas for data manipulation.
- numpy, matplotlib, and seaborn for data analysis and visualization (used in the recommender system).
Spotify API: Authentication and data retrieval.

## Getting Started

### Setup

Clone the repository:

```bash
git clone https://github.com/your-username/spotify-data-and-recommender.git
cd spotify-data-and-recommender
```

Set up Spotify Developer Credentials:

- Go to the Spotify Developer Dashboard.
- Create an application to get your CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI.
- Store these values in environment variables or replace the placeholders in User Data Extraction.py.

Install dependencies:

```bash
pip install spotipy pandas matplotlib seaborn
```

### Running the Projects

#### User Data Extraction:

Run the Python script:
```bash
python User\ Data\ Extraction.py
```
A CSV file (spotify_tracks_f.csv) will be generated with all extracted data.

#### Song Recommender:

Open the Jupyter Notebook:
```bash
jupyter notebook Song\ Recommender.ipynb
```
Follow the steps in the notebook to load data and generate recommendations.


