import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import pydeck as pdk
from shapely.geometry import Point, Polygon
import geopandas as gpd
import pandas as pd
import geopy

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

st.set_page_config(layout="wide",
                    page_title="Too Good To Code",
                    page_icon="😎",
                    initial_sidebar_state="expanded",
                    menu_items={
                        'Get Help': 'https://www.github.com/nathanyaqueby/too-good-to-code',
                        'Report a bug': "https://www.github.com/nathanyaqueby/too-good-to-code/issues",
                        'About': "# Welcome to Too Good To Code!"
                    })

st.title("Genistat's Solar Challenge")
# st.markdown("## Welcome to Too Good To Code!")

with st.sidebar.form(key='my_form'):
    st.title("Initialize the map")

    st.info("""
            Pinpoint your location and generate a preliminary map of the solar efficiency.
            """, icon="🗒️")

    # country_names = pd.read_csv("data/average-latitude-longitude-countries.csv")["Country"].values.tolist()

    # # set up a dropdown menu to select the country of interest
    # country = st.selectbox("Select a country", country_names, index=country_names.index('Germany'))

    # # set up a slider to select the number of panels
    # num_panels = st.slider("Select the number of panels", 0, 100, 50)

    # # set up a slider to filter the efficiency
    # efficiency = st.slider("Select the efficiency", 0.0, 1.0, 0.5, 0.01)

    # # add radio buttons to show the raster or the vector map
    # map_type = st.radio("Select the map type", ("Raster", "Vector"), horizontal=True)

    street = st.sidebar.text_input("Street", "Altenbergerstrasse 69")
    city = st.sidebar.text_input("City", "Linz")
    province = st.sidebar.text_input("Province", "Upper Austria")
    country = st.sidebar.text_input("Country", "Austria")

    geolocator = Nominatim(user_agent="GTA Lookup")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(street+", "+city+", "+province+", "+country)

    lat = location.latitude
    lon = location.longitude

    map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})

    # create a submit button to retrain the model
    loc = st.form_submit_button("Visualize location", type="primary", use_container_width=True)

with st.sidebar.form(key='download'):
    st.title("Solar Efficiency Report")

    st.markdown("Save all the results of the solar efficiency analysis and the visualizations in a PDF file.")

    # create a submit button to download the retrained model
    if st.form_submit_button("Download as PDF", type="secondary", use_container_width=True):
        st.write("Downloaded!")

st.sidebar.markdown("---")
st.sidebar.markdown("Read more about the project on [GitHub](www.github.com/nathanyaqueby/too-good-to-code).")

if loc:
    st.map(map_data) 
else:  
    components.html("""
            <html>
            <head>
            </head>

            <iframe height="700" style="width: 100%;" scrolling="no" title="OSM Buildings" src="https://codepen.io/nqueby/embed/vYVJJGz?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
            See the Pen <a href="https://codepen.io/nqueby/pen/vYVJJGz">
            OSM Buildings</a> by Nathanya Queby Satriani (<a href="https://codepen.io/nqueby">@nqueby</a>)
            on <a href="https://codepen.io">CodePen</a>.
            </iframe>

            </html>
            """,
            height=700,
            scrolling=True
            )