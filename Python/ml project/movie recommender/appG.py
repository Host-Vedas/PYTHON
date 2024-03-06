import streamlit as st
import pandas as pd
import pickle

st.title('Movie Recommender System')

movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies_list
)

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies_list[i[0]] for i in movie_list]
    return recommended_movies

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
