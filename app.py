import streamlit as st
import pickle
import pandas as pd
import requests



def fetch_poster(movie_id):
    respose = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=04b740abaf4e708f58e629a195528188'.format(movie_id))
    data = respose.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id =movies.iloc[i[0]].movie_id
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters



movies_dict = pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)


st.title('Movie Recommendation System')
selected_movie_name = st.selectbox('Type or select a movie form the dropdown',
                      movies['title'].values)



if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    row1 = st.columns(5)
    row2 = st.columns(5)

    with row1[0]:
        st.image(recommended_movie_posters[0],caption=recommended_movie_names[0])
    with row1[1]:
        st.image(recommended_movie_posters[1], caption=recommended_movie_names[1])

    with row1[2]:
        st.image(recommended_movie_posters[2], caption=recommended_movie_names[2])
    with row1[3]:
        st.image(recommended_movie_posters[3], caption=recommended_movie_names[3])
    with row1[4]:
        st.image(recommended_movie_posters[4], caption=recommended_movie_names[4])
    with row2[0]:
        st.image(recommended_movie_posters[5], caption=recommended_movie_names[5])
    with row2[1]:
        st.image(recommended_movie_posters[6], caption=recommended_movie_names[6])
    with row2[2]:
        st.image(recommended_movie_posters[7], caption=recommended_movie_names[7])
    with row2[3]:
        st.image(recommended_movie_posters[8], caption=recommended_movie_names[8])
    with row2[4]:
        st.image(recommended_movie_posters[9], caption=recommended_movie_names[9])


