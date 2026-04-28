import streamlit as st
import pickle
import requests
import requests
from time import sleep

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{movie_id}?api_key=69d31f953936f15e12f1834f2e2fd1bf"
from time import sleep

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{movie_id}?api_key=69d31f953936f15e12f1834f2e2fd1bf"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Raises HTTPError for bad responses
            data = response.json()
            return data['poster_path']  # Adjust this depending on the structure
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1} failed: {e}")
            sleep(2)

    print("Failed to fetch poster after multiple attempts.")
    return None
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Raises HTTPError for bad responses
            data = response.json()
            return data['poster_path']  # Adjust this depending on the structure
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1} failed: {e}")
            sleep(2)

    print("Failed to fetch poster after multiple attempts.")
    return None


def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=69d31f953936f15e12f1834f2e2fd1bf&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values

st.header("Movie Advisory System")

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
   
    ]


imageCarouselComponent(imageUrls=imageUrls, height=200)
selectvalue=st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster



if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
