# Movie-Advisory-System-Using-Content-Based-Filtering
A machine learning-based recommendation engine that suggests movies similar to a user's choice using Natural Language Processing (NLP) and vector similarity.

🚀 Features
Content-Based Filtering: Recommends movies by analyzing metadata (Cast, Crew, Genres, Keywords).

NLP Pipeline: Implemented text preprocessing including Stemming and Count Vectorization.

Similarity Engine: Uses Cosine Similarity to measure the distance between movie vectors.

Web Interface: Interactive UI built with Streamlit.

Real-time Data: Fetches movie posters and details via the TMDB API.

🛠️ Technical Stack
Language: Python

Libraries: Pandas, NumPy, NLTK, Scikit-learn

Frontend: Streamlit

Deployment: Pickle (for model serialization)

📊 Dataset
The system uses the TMDB 5000 Movie Dataset, involving extensive data cleaning and merging of movie features into a unified "tags" system.
