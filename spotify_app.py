import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from IPython.display import IFrame
import random
from fuzzywuzzy import process
import pandas as pd  # Assuming df_final and top_100 are pandas DataFrames

# Load your configuration (replace with your actual config loading)
import config  # Assuming you have a config.py file with client_id and client_secret

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.client_id,
                                                           client_secret=config.client_secret))

df_final = pd.read_csv('df_final.csv')

top_100 = pd.read_csv('top_100.csv')

def perform_trending_action():
    print("Here's a song from 'trending'")
    random_row = top_100.sample()
    random_search_song = random_row['Song'].values[0]
    random_search_artist = random_row['Artist'].values[0]
    random_search = f"{random_search_song} - {random_search_artist}"
    
    # Perform the search and store the result in 'results'
    results = sp.search(q=random_search, limit=1) 
    
    if results['tracks']['items']:
        track_id = results["tracks"]["items"][0]["id"]
        embed_url = f"https://open.spotify.com/embed/track/{track_id}"
        iframe_html = f'<iframe src="{embed_url}" width="320" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'
        return iframe_html
    else:
        st.write("Song not found on Spotify.")
        return None

def perform_genre_action(genre, df_final):
    print(f"Here's a song from {genre}")

    # Filter the DataFrame and store the result in 'filtered_df'
    filtered_df = df_final[df_final['genre'] == f"{genre}"] 

    if not filtered_df.empty:
        random_song = filtered_df.sample(n=1)
        track_id = random_song['track_id'].values[0]
        embed_url = f"https://open.spotify.com/embed/track/{track_id}"
        iframe_html = f'<iframe src="{embed_url}" width="320" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'
        return iframe_html
    else:
        st.write(f"No songs found for the genre {genre}.")
        return None

genres = ['trending', 'Energetic Pop/Rock', 'Acoustic & Mellow Melodies', 'Upbeat Grooves', 'Energetic Instrumental Grooves', 'Global Pop Fusion', 'Chill Mix', 'Alternative Indie']

def check_input(input_string):
    match, score = process.extractOne(input_string.lower(), genres)

    if score >= 80:
        if match == 'trending':
            iframe_html = perform_trending_action()
            if iframe_html:
                st.components.v1.html(iframe_html, height=80)  # Correct indentation
        elif match in genres:
            iframe_html = perform_genre_action(match, df_final)
            if iframe_html:
                st.components.v1.html(iframe_html, height=80)  # Correct indentation
    else:
        st.write(f"'{input_string}' didn't match any results. Please try again.")

st.title("Song Genre Explorer")
st.header("Choose a genre to listen to:")

for genre in genres:
    if st.button(genre):
        check_input(genre)