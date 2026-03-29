# Simple Movie Recommender Database
Simple Movie Recommender & Database is a command-line application built in Python that allows users to manage a local database of movies and receive movie recommendations.

The application stores movie details (Title, Genre, Description) in a local JSON file (movies_data.json). The core feature is the recommendation engine, which uses the TF-IDF (Term Frequency-Inverse Document Frequency) technique to convert movie descriptions into numerical feature vectors. It then calculates the Cosine Similarity between the description vectors to find and suggest movies most similar to a user-selected title.

This project is an excellent example of a basic content-based recommendation system implementation using fundamental Machine Learning concepts.

# Features
-CRUD Operations: Add, View, Update, and Delete movie records.

-Data Persistence: Stores and retrieves all movie data using a local movies_data.json file.

-Content-Based Recommendation: Suggests the top 5 most similar movies based on the textual similarity of their descriptions.

-Interactive Menu: Easy-to-use console interface.

# Installation
To run this project, you need Python and the necessary libraries installed.

Prerequisites
-Python 3.x

1.Clone the repository:
git clone https://github.com/YourUsername/Simple-Movie-Recommender.git
cd Simple-Movie-Recommender

2.Install Dependencies: The project relies on scikit-learn for the recommendation engine.
pip install scikit-learn
(Note: json and os are built-in Python libraries and do not require separate installation.)

# Usage
1.Run the application:
python your_script_name.py
(Replace your_script_name.py with the actual name you saved the code as.)

2.Interactive Menu: The application will present a main menu:
=== Movie App ===
1. Add movie
2. Show all
3. Update movie
4. Delete movie
5. Recommend similar movies
0. Exit
Choose:

3.Recommendation Workflow (Option 5):
-First, add at least two movies using option 1.

-Select option 5. The application will list all saved movies with their IDs.

-Enter the ID of the movie you want suggestions for.

-The system will calculate similarity based on the movie descriptions and output the top 5 recommendations with a match score.

# Technology Stack
1)Language: Python 3

2)Libraries:
-sklearn.feature_extraction.text.TfidfVectorizer: To generate feature vectors from text data.
-sklearn.metrics.pairwise.cosine_similarity: To calculate the similarity between movie description vectors.

3)Data Storage: Local JSON file (movies_data.json).

# Contributing
Contributions are welcome! If you have suggestions for improving the recommendation accuracy (e.g., adding Genre to the TF-IDF vectorization) or enhancing the UI, feel free to open an issue or submit a pull request.

-Fork the repository.

-Create a new branch (git checkout -b feature/improvement).

-Make your changes and commit (git commit -m 'Add new feature').

-Push to the branch (git push origin feature/improvement).

-Open a Pull Request.

# Author:
Vishwa Namdeo Badgujar
