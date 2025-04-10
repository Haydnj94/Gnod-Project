
# 🎵 Mood-Based Music Recommender

This is a Python-based project that recommends songs to users based on their current **mood** using the **Spotify Web API**. The project provides genre and mood-based song suggestions to enhance user experience with personalized playlists.

## 🚀 Features

- Recommend songs based on mood categories
- Uses the Spotify API to fetch real-time song data
- Supports multiple genres
- Easy-to-use interactive notebook

## 📁 Project Structure

- `Gnod-Project.ipynb`: Jupyter Notebook with the main logic and user interaction
- `config.py`: File where you store your personal Spotify API credentials
- `requirements.txt`: (optional – add this if you want to list dependencies)

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set up your Spotify API credentials

To use this project, you must have a **Spotify Developer account** and create an app to get your credentials:

- Visit: https://developer.spotify.com/dashboard/
- Log in and create an app
- Copy the **Client ID** and **Client Secret**

Then, create a file named `config.py` in the root directory with the following content:

```python
SPOTIPY_CLIENT_ID = "your_client_id_here"
SPOTIPY_CLIENT_SECRET = "your_client_secret_here"
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"
```

> ⚠️ **Important:** For security reasons, do **NOT** commit your `config.py` file to GitHub.
>
> Add it to your `.gitignore` file:

```
config.py
```

### 3. Install required libraries

You can install the required dependencies using pip:

```bash
pip install spotipy
```

Or use a requirements file (if included):

```bash
pip install -r requirements.txt
```

### 4. Run the notebook

Open the notebook in Jupyter:

```bash
jupyter notebook Gnod-Project.ipynb
```

Follow the prompts to select your mood, and the system will recommend songs based on your selection!

## 💡 Example Moods & Genres

The notebook provides predefined mood options mapped to specific music genres. Explore different moods to discover new tracks tailored to your vibe.


## 🤖 Machine Learning Integration

This project uses **KMeans Clustering** to group songs into different clusters based on audio features provided by the Spotify API. These clusters represent various moods or genres, and help in providing more accurate and dynamic recommendations.


## 🌐 Web App Deployment

The application is also deployed using **Streamlit**, allowing users to interact with the recommender system through a web interface.

To run the web app:

```bash
streamlit run spotify_app.py
```

Make sure your `config.py` with Spotify credentials is in the same directory.

## ✅ To Do / Future Improvements

- Add audio preview for each track
- Improve mood classification with ML
- Build a web interface
