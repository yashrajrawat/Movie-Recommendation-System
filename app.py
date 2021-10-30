from requests.models import Response
import streamlit as st
import pickle
import pandas as pd
import requests

#setting streamlit layout to wide open
st.set_page_config(layout="wide")

#title of the project
st.title('Movie Recommender System')
title_alignment="""
<style>
#the-title {
  text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

#loading pickle files
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=79831a5f5ff447d36aa038d77367d6d1&language=en-US".format(movie_id),verify=False)
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),key=lambda x:x[1],reverse=True)[1:11]
    
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movies_id=movies.iloc[i[0]].movie_id
        #Fetching Poster From API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies_id))
    return recommended_movies, recommended_movies_posters



selected_movie_name=st.selectbox(
"Enter / Select a Movie",
movies['title'].values)

import base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
.stApp {
  background-image: url("data:image/png;base64,%s");
  background-size: cover;
}
</style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('static/img/background.png')


if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)

    col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
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
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])

import webbrowser



footer="""<style>
a:link , a:visited{
color: orange;
background-color: transparent;
}

a:hover,  a:active {
color: blue;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/yashraj-singh-rawat/" target="_blank">Yashraj Singh Rawat</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
