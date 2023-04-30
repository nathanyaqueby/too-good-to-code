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

    street = st.text_input("Street", "Rathausmarkt 1")
    city = st.text_input("City", "Hamburg")
    province = st.text_input("Province", "Hamburg")
    country = st.text_input("Country", "Germany")

    geolocator = Nominatim(user_agent="GTA Lookup")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(street+", "+city+", "+province+", "+country)

    lat = location.latitude
    lon = location.longitude

    st.write("Latitude: ", lat)
    st.write("Longitude: ", lon)

    # map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})

    # sat_img = save_satellite_image(lat, lon)

    # center on Liberty Bell, add marker
    m = folium.Map(location=[lat, lon], zoom_start=16)
    folium.Marker(
        [lat, lon], popup="Selected location", tooltip="Selected location"
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

# download section
# with st.sidebar.form(key='download'):
#     st.title("Solar Efficiency Report")

#     st.markdown("Save all the results of the solar efficiency analysis and the visualizations in a PDF file.")

#     # create a submit button to download the retrained model
#     if st.form_submit_button("Download as PDF", type="secondary", use_container_width=True):
#         st.write("Downloaded!")

# st.sidebar.markdown("---")
# st.sidebar.markdown("Read more about the project on [GitHub](www.github.com/nathanyaqueby/too-good-to-code).")
st.sidebar.image("img/too good to code.png", use_column_width=True)

if loc:

    # add three columns to the main page with explanations on the solar efficiency
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("### Satellite Image")
        # col1.image(sat_img, use_column_width=True)
        # col1.map(map_data, zoom=16, use_container_width=True) 
        
        st_data = st_folium(m, zoom=16, width=640, height=640)

        # col1.markdown("The ratio between the energy produced by the solar panels and the energy received by the sun.")
        # col1.markdown("It is computed as follows:")
        # col1.latex(r'''
        #             \eta = \frac{E_{panels}}{E_{sun}}
        #             ''')
    
    # col2.markdown("### Amount of Energy Produced")
    # col2.markdown("A function of the solar efficiency and the energy received by the sun.")
    # col2.markdown("It is computed as follows:")
    # col2.latex(r'''
    #             E_{panels} = \eta \times E_{sun}
    #             ''')
    
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
        col2.markdown("📍 Location: "+str(location.address))
        col2.markdown(f"📐 Solar area: {solar_area} m^2")
        col2.markdown(f"☀️ Sun radiation: {radiance} kwh/m^2")
        col2.markdown(f"🌱 Solar efficiency: 4.2/10")
        col2.markdown(f"⚡ Electric potential: {energy_produced} kwh")

    with col3:
        st.markdown("### Heatmap")
        # plot the radiance heatmap for the city of Hamburg based on the dataframe
        fig = px.density_mapbox(df, lat="center_lat", lon="center_long", z="radiance", radius=10, zoom=10, mapbox_style="stamen-terrain")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)


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