import streamlit as st
import requests

def save_satellite_image(lat, long, file='pic.jpg', zoom=20):
    # Enter your api key here
    api_key = st.secrets["API_TOKEN"]

    # url variable store url
    url = "https://maps.googleapis.com/maps/api/staticmap?"

    center = f"{lat},{long}"

    r = requests.get(url + "center=" + center + "&zoom=" +
                   str(zoom) + "&maptype=satellite" + "&size=640x640&key=" +
                             api_key )

    # wb mode is stand for write binary mode
    f = open(file, 'wb')

    # r.content gives content,
    # in this case gives image
    f.write(r.content)

    f.close()

    return file