import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_poster(movie_id):
    # response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2c8a2c8b091ef86cc267ce219dbe85d7&language=en-US'.format(movie_id))
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2c8a2cb091ef86cc267ce219dbe85d7'.format(movie_id))
    data = response.json()

    poster_path = data.get('poster_path', None)

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return None


st.title('Movie Recommender System')

movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

Selected_Movie_Name = st.selectbox(
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
    recommendations = recommend(Selected_Movie_Name)
    posters = [fetch_poster(movie_id) for movie_id in recommendations]

    col1, col2, col3, col4, col5 = st.columns(5)

    for i in range(len(recommendations)):
        with col1, col2, col3, col4, col5:
            if posters[i] is not None:
                st.text(recommendations[i])
                st.image(posters[i])
            else:
                st.text("No poster available for {}".format(recommendations[i]))

