from http.client import responses

import streamlit as st
import pickle
import requests


#function for movie recommendation
def recommend(movie):
    movie_index = movies_list1[movies_list1['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        #fetching poster
        movie_id = i[0]
        recommended_movies.append(movies_list1.iloc[i[0]].title)

    return recommended_movies


movies_list1 = pickle.load(open('movies.pkl','rb'))
movies = movies_list1['title'].values
st.title('Movie Recommender System')

similarity = pickle.load(open('similarity.pkl','rb'))

#text box for user
selected_movie_name = st.selectbox(
'What type of movie do you prefer?',
(movies))

#button
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)














