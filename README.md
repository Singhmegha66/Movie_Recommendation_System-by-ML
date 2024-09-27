# Movie_Recommendation_System-by-ML
his project implements a Content-Based Movie Recommendation System using the TMDB 5000 Movie Dataset from Kaggle. The system is built using machine learning in a Jupyter Notebook for data preprocessing, cleaning, and model creation. The front-end is developed using PyCharm to provide an interactive user interface for movie recommendations.

🔑 Key Features
Content-Based Recommendation:
The system recommends movies based on the similarity of content such as genres, keywords, and descriptions.

Data Cleaning & Preprocessing:
The dataset undergoes a thorough cleaning and preprocessing step to ensure reliable and accurate movie recommendations.

Interactive Front-End:
A user-friendly interface built using PyCharm allows users to input a movie name and receive personalized recommendations based on the selected movie.

🗂️ Dataset
The project uses the TMDB 5000 Movie Dataset from Kaggle, which includes over 5000 movies with details such as:

Movie title
Overview (plot description)
Genres
Cast and crew
Keywords
Link to the dataset: TMDB 5000 Movie Dataset

📊 Steps in the Project
1. Data Cleaning & Preprocessing (Jupyter Notebook)
Before building the recommendation system, the raw data from the TMDB dataset was cleaned and preprocessed. The key steps include:

Handling Missing Data:
Removed or filled missing values in important columns such as movie titles and genres.

Text Preprocessing:
Cleaned and processed text data (such as movie overviews and genres) by tokenizing, removing stop words, and stemming keywords to improve content similarity measures.

Feature Engineering:
Combined multiple features like genres, keywords, and movie overviews to create a unified text feature for each movie, representing its content.

Similarity Matrix Creation:
Using the cleaned data, a TF-IDF Vectorizer was applied to create a matrix representing the similarity between movies based on their content.

2. Building the Recommendation Model
A Content-Based Filtering approach was employed to create the recommendation system. The steps involved:

TF-IDF Vectorization:
Transformed the movie overviews and other textual content into numerical vectors using the TF-IDF vectorizer, which helps in calculating movie similarity.

Cosine Similarity Calculation:
Calculated the cosine similarity between all movies in the dataset based on their TF-IDF vectors. This similarity measure helps in identifying movies that are closest in content to the input movie.

Recommendation Function:
A function was implemented to take a movie name as input and return a list of movies similar in content based on the highest cosine similarity scores.

3. Front-End Development (PyCharm)
The front-end interface was built using PyCharm, where users can input a movie name to receive recommendations. The user interface interacts with the machine learning model to provide real-time movie suggestions. Key technologies used:

Flask for backend handling
HTML/CSS/JavaScript for creating a clean and intuitive user interface.
🛠️ Tools & Technologies
Jupyter Notebook:
For data cleaning, preprocessing, and building the recommendation model using Python.

PyCharm:
Used for developing the front-end interface and integrating it with the recommendation system.

Libraries Used:

Pandas for data manipulation and analysis.
NumPy for numerical operations.
Scikit-learn for TF-IDF vectorization and cosine similarity.
NLTK (Natural Language Toolkit) for text preprocessing.
