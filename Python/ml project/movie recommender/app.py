import streamlit as st
import pandas
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['posterpath']

st.title('Movie Recommender System')

movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list['title'].values

similirity = pickle.load(open('similarity.pkl','rb'))

Selected_Movie_Name = st.selectbox(
    'How Would you like to be connected?',
    (movies_list)
)
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similirity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recomended_movies = []
    recomended_movies_poster = []
    for i in movie_list:
        movie_id = movie_list.iloc[i[0]]

        recomended_movies.append(movie_list.iloc[i[0]].title)
        # fetch poster from api
        recomended_movies_poster.append(fetch_poster(i[0]))
    return recomended_movies

if st.button('Recommend'):
    names,poster =recommend(Selected_Movie_Name)
    col1,col2,col3,col4,col5 = st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
    for i in recomendations:
        st.write(i)





