Welcome to the Spotify Project! 🎵

After reading the Gnoosic Project Introduction, you are now ready to develop the new music recommendation system that Jane, the CTO of Gnoosic, asked you to create.

This interactive music recommender will be tested live on Friday, where we will assess how well your song recommendations match user preferences! 🚀

Instructions

DAY 1: Collecting Data 📊
Objective:
1️⃣ Scrape trending songs:

Scrape the Billboard Hot 100 (Billboard Charts) to collect the top 100 songs and respective artists.
Store this in a DataFrame with the columns:
"song_title" and "artist"
These songs will form a "Trending" category that users can choose from.

2️⃣ Gather audio features:

Explore the dataset that is provided to you, making sure you understand what each column means. Keep in mind that this knowledge will be precious for the machine learning part!

DAY 2: Basic Recommendation System Setup 🤖
Objective:
1️⃣ User Song Type Selection (Basic Recommender Prototype)

Create a program where the user can input a music type rather than a specific song.
The user can choose from:
"High Energy", "Chill Vibes", "Rock", "Trending Now", etc.
For now, if the user selects "Trending Now," return a random popular song from the Billboard Hot 100 DataFrame.
If they select another type, simply acknowledge their selection (without returning a song yet).

DAY 3: Clustering Songs for Personalized Recommendations 🎧
Objective:
1️⃣ Cluster songs based on their musical characteristics

Use unsupervised learning (e.g., K-Means, DBSCAN, Hierarchical Clustering) to group similar songs.
Identify 5 to 20 natural clusters in your dataset based on audio features.
Assign a cluster ID to each song in the dataset.
2️⃣ Label the Clusters (Genre & Mood-Based Categorization)

Explore each cluster and assign a descriptive label (e.g., "Rock", "High Energy", "Chill Vibes").
These labels will be used so that when a user selects a music type, they get a song from that cluster.

DAY 4: Finalizing the Music Recommender 🔥
Objective:
1️⃣ Final Song Recommendation System

The program should now recommend a song based on the user’s chosen music type:
If the user selects "Trending Now", return a random trending song from the Billboard Hot 100 list.
If they select another category (e.g., "Chill Vibes", "Rock", "High Energy"), return a random song from the corresponding cluster.
2️⃣ Live Testing & Presentation

Be ready to demo your system on Friday to Jane and the team.
Explain your clustering strategy and how you labeled the clusters.

