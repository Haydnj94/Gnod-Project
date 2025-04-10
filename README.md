# 🎧 Mood-Based Music Recommender: Discover Your Vibe!

This project is a Python-based music recommendation system designed to suggest songs based on your current **mood** and preferences. By leveraging data analysis, machine learning techniques, and the **Spotify Web API**, this recommender aims to provide personalized and enjoyable listening experiences.

---

## ✨ Key Features

- **Mood-Based Recommendations:** Get song suggestions tailored to your chosen mood or genre.
- **Trending Music Integration:** Explore the latest hits from the Billboard Hot 100.
- **Clustering for Personalization:** Utilizes unsupervised learning (e.g., K-Means) to group songs with similar audio characteristics.
- **Genre & Mood Mapping:** Clusters are labeled with mood types like *High Energy*, *Chill Vibes*, *Rock*, etc.
- **Spotify API Integration:** Fetch real-time song data and audio features using the Spotify API.
- **Interactive User Experience:** Easy-to-use interface (initially via Jupyter Notebook) for selecting moods and receiving recommendations.
- **Web Deployment:** Deployed as a web application using **Streamlit**.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

### 2. Obtain Spotify API Credentials

	1.	Go to Spotify Developer Dashboard.
	2.	Log in or sign up.
	3.	Create a new app.
	4.	Note down the Client ID and Client Secret.

### 3. Configure Spotify API Credentials

	1.	Open the 'config.py' file.
	2.	Add your API credentials within the quotations (client_id = "" + client_secret = "")

 ⚠️ Important: Add config.py to .gitignore to protect your credentials

### 4. Install Dependencies

If requiered, run 'pip install -r requirements.txt' in a notebook cell to install the requiered dependencies.

### 5. Run the Jupyter Notebook

Open the jupyter notebook 'Gnod-Project.ipynb' and follow on-screen prompts to select your mood and receive recommendations.

### 6. Run the Streamlit Web Application

This launches the app in your browser by running 'streamlit run spotify_app.py' from the Terminal. Make sure config.py is in the same directory if using Spotify.

## 💡 How It Works: From Data to Recommendations

Data Collection
	•	Trending Songs: Scraped from Billboard Hot 100.
	•	Audio Features: Dataset contains features like energy, tempo, and danceability.

Basic Recommendation Logic
	•	User selects a mood or genre:
	•	If “Trending Now” → return a random Billboard Hot 100 song.
	•	If other types → recommend from matching clusters.

Clustering for Personalization
	•	Algorithm: K-Means or similar.
	•	Clustering: Songs are grouped by audio similarity.
	•	Labeling: Clusters are manually labeled (e.g., Chill Vibes, High Energy).

Final Recommendation

Based on user selection:
	•	Trending Now: Random Billboard song.
	•	Mood/Genre: Random song from matching cluster.

🤖 Machine Learning Implementation
•	Unsupervised Learning: K-Means from scikit-learn.
•	Features: Audio metrics from Spotify or dataset.
•	Goal: Create dynamic categories based on musical similarity.
