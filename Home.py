import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.mention import mention
import pandas as pd
import numpy as np
import pydeck as pdk
from shapely.geometry import Point, Polygon
import geopandas as gpd
import pandas as pd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import plotly.express as px
from streamlit_folium import st_folium
import folium

from preprocessing import save_satellite_image


st.set_page_config(layout="wide",
                    page_title="Too Good To Code",
                    page_icon="😎",
                    initial_sidebar_state="expanded",
                    menu_items={
                        'Get Help': 'https://www.github.com/nathanyaqueby/too-good-to-code',
                        'Report a bug': "https://www.github.com/nathanyaqueby/too-good-to-code/issues",
                        'About': "# Welcome to Too Good To Code!"
                    })

st.markdown("""
    <style>
    .css-8hkptd {
            margin-right: 15px;
        }
    </style>""", unsafe_allow_html=True)

st.title("Genistat's Solar Challenge")
# st.markdown("## Welcome to Too Good To Code!")

with st.sidebar.form(key='my_form'):
    st.title("Initialize the map")

    st.info("""
            Pinpoint your location and generate a preliminary map of the solar efficiency.
            """
            # , icon="🗒️"
            )

    country_names = pd.read_csv("data/average-latitude-longitude-countries.csv")["Country"].values.tolist()

    # # set up a dropdown menu to select the country of interest
    # country = st.selectbox("Select a country", country_names, index=country_names.index('Germany'))

    # # set up a slider to select the number of panels
    # num_panels = st.slider("Select the number of panels", 0, 100, 50)

    # # set up a slider to filter the efficiency
    # efficiency = st.slider("Select the efficiency", 0.0, 1.0, 0.5, 0.01)

    # # add radio buttons to show the raster or the vector map
    # map_type = st.radio("Select the map type", ("Raster", "Vector"), horizontal=True)

    # load data
    df = pd.read_csv("data/final/solar_hamburg_short.csv")
    df_berlin = pd.read_csv("data/final/solar_berlin.csv")
    df_bremen = pd.read_csv("data/final/solar_bremen.csv")

    street = st.text_input("Street", "Rathausmarkt 1")
    # set up a dropdown menu to select the state between Hamburg, Berlin and Bremen
    province = st.selectbox("Select a state", ["Hamburg", "Berlin", "Bremen"], index=0)
    country = "Germany"

    city = "Hamburg" if province == "Hamburg" else "Berlin" if province == "Berlin" else "Bremen"

    geolocator = Nominatim(user_agent="GTA Lookup")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(street+", "+city+", "+province+", "+country)

    lat = location.latitude
    lon = location.longitude

    # add a slider to select the budget in euros
    budget = st.slider("Select the budget in euros (€)", 0, 100000, 50000)

    # st.write("Latitude: ", lat)
    # st.write("Longitude: ", lon)

    map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})

    # sat_img = save_satellite_image(lat, lon)

    # center on Liberty Bell, add marker
    m = folium.Map(location=[lat, lon], zoom_start=16)
    folium.Marker(
        [lat, lon], popup="Selected location", tooltip="Selected location"
    ).add_to(m)

    top_100 = df.sort_values(by=["solar_area", "radiance"], ascending=False).head(100)

    # add markers to the map if user checks "Show top 100 locations"
    if st.checkbox("Show top 100 locations"):
        for i in range(100):
            folium.Marker(
                [top_100["center_lat"].iloc[i], top_100["center_long"].iloc[i]], popup="Top 100", tooltip="Top 100"
            ).add_to(m)

    # create a submit button to retrain the model
    loc = st.form_submit_button("Visualize location", type="primary", use_container_width=True)

# tech support section
with st.sidebar.form(key='tech_support'):
    st.title("Contact")

    st.markdown("Get help with any technical issue you might experience.")

    mention(
    label="Website",
    icon="💻",
    url="https://www.genistat.ch",
    write="Website"
    )

    mention(
    label="Twitter",
    icon="🐤",
    url="https://twitter.com/neuronaiAustria",
    write="Twitter"
    )

    mention(
    label="GitHub",
    icon="⚙️",
    url="https://www.github.com/nathanyaqueby/too-good-to-code",
    write="GitHub"
    )

    mention(
    label="24/7 Support",
    icon="☎️",
    url="https://www.linkedin.com/in/hari-kesavan",
    write="24/7 Support"
    )

    # create a submit button
    if st.form_submit_button("Contact us", type="secondary", use_container_width=True):
        st.write("Submitted!")

st.sidebar.image("img/too good to code.png", use_column_width=True)

# add three columns to the main page with explanations on the solar efficiency
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("### Satellite Image")
    # col1.image(sat_img, use_column_width=True)
    # col1.map(map_data, zoom=16, use_container_width=True) 

    # get the sum of the radiance from each dataframe and print the result
    # st.write("Total radiance: ", round(df["radiance"].sum(), 2))
    # st.write("Total radiance: ", round(df_berlin["radiance"].sum(), 2))
    # st.write("Total radiance: ", round(df_bremen["radiance"].sum(), 2))
    
    st_data = st_folium(m, width=640, height=640)
    

with col2:
    st.markdown("### Details")
    round_num = 2
    center_lat = round(df["center_lat"], round_num)
    center_long = round(df["center_long"], round_num)
    round_lat = round(lat, round_num)
    round_lon = round(lon, round_num)
    # get the solar_area, energy_produced, and radiance based on the closest latitude and longitude
    try:
        solar_area = df.loc[(center_lat == round_lat) & (center_long == round_lon)]["solar_area"].values[0]
        energy_produced = df.loc[(center_lat == round_lat) & (center_long == round_lon)]["energy_produced"].values[0]
        radiance = df.loc[(center_lat == round_lat) & (center_long == round_lon)]["radiance"].values[0]
    except IndexError:
        round_num -= 1
        center_lat = round(df["center_lat"], round_num)
        center_long = round(df["center_long"], round_num)
        round_lat = round(lat, round_num)
        round_lon = round(lon, round_num)
        solar_area = df.loc[(center_lat == round_lat) & (center_long == round_lon)]["solar_area"].values[0]
        energy_produced = df.loc[(center_lat == round_lat) & (center_long == round_lon)]["energy_produced"].values[0]
        radiance = df.loc[(center_lat == round_lat) & (center_long == round_lon)]["radiance"].values[0]

    # list the location, area (m^2), sun radiation (kwh/m^2), solar efficiency (0-10), and amount of electric potential (kwh)
    st.markdown("📍 Location: "+str(location.address))
    st.markdown(f"📐 Solar area: {solar_area} m^2")
    st.markdown(f"☀️ Sun radiation: {radiance} kwh/m^2")
    st.markdown(f"🌱 Solar efficiency: 4.2/10")
    st.markdown(f"⚡ Electric potential: {energy_produced} kwh")

    # display the top 100 buildings with the largest roofs and best efficiency per square meter from df
    st.markdown("---")
    st.markdown("### Top 100 Buildings")
    st.markdown(f"Buildings with the largest roofs and best efficiency per square meter in {province}.")
    # get the top 100 buildings from df and display them in a table

    # add a button to display the top 100 buildings
    if st.checkbox("Display dataframe"):
        st.dataframe(top_100, use_container_width=True, height=120)

    # add the top buildings from top_100 to the map
    for i in range(len(top_100)):
        folium.Marker(
            [top_100.iloc[i]["center_lat"], top_100.iloc[i]["center_long"]], popup="Top 100", tooltip="Top 100"
        ).add_to(m)

    # display the last clicked location from the st_data dict
    st.markdown("---")

    # create two subcolumns
    col21, col22 = st.columns(2)

    with col21:	
        st.markdown("### Last Clicked Location")
        try:
            st.write("Latitude: ", st_data["last_clicked"]["lat"])
            st.write("Longitude: ", st_data["last_clicked"]["lng"])
        except TypeError:
            st.markdown("Select the precise point on the map and you should see the latitude and longitude here.")
    
    with col22:
        # add metric
        st.markdown("### Predicted Solar Potential")
        # add suggested solar panel amount and energy produced
        st.markdown("The suggested solar panel amount is 2.")
