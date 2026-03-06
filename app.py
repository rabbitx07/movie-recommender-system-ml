import streamlit as st
import pickle
import requests
import os
import gdown

FILE_ID = "1B-Uymv3K2M473frYGGrQN6e70ta6P9uc"

# delete corrupted file if HTML got downloaded
if os.path.exists("similarity.pkl") and os.path.getsize("similarity.pkl") < 1000000:
    os.remove("similarity.pkl")

# download if missing
if not os.path.exists("similarity.pkl"):
    gdown.download(id=FILE_ID, output="similarity.pkl", quiet=False)
api_key = st.secrets["TMDB_API_KEY"]

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url)
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except:
        return "https://via.placeholder.com/500x750?text=Poster+Not+Found"


def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = new_df.iloc[i[0]]['id']

        recommended_movies.append(new_df.iloc[i[0]].title)

        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


new_df = pickle.load(open('movies.pkl','rb'))
movies_list = new_df['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox('Select a movie', movies_list)

if st.button('Recommend'):
    names,posters = recommend(selected_movie)


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

st.markdown("""
---
<div style="text-align:center; color:grey; font-size:14px;">
 AI Movie Recommender <br>
Built with <b>Python, Scikit-Learn, Streamlit & TMDB API</b><br><br>

Created by <b>Anshika</b> | 
<a href="https://github.com/rabbitx07/movie-recommender-system-ml" target="_blank">
GitHub Repository
</a>
</div>
""", unsafe_allow_html=True)
