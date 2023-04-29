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
            margin-right: 13px;
        }
    </style>""", unsafe_allow_html=True)

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

    street = st.text_input("Street", "Altenbergerstrasse 69")
    city = st.text_input("City", "Linz")
    province = st.text_input("Province", "Upper Austria")
    country = st.text_input("Country", "Austria")

    geolocator = Nominatim(user_agent="GTA Lookup")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(street+", "+city+", "+province+", "+country)

    lat = location.latitude
    lon = location.longitude

    map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})

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
    st.map(map_data, zoom=16, use_container_width=True) 

    # add three columns to the main page with explanations on the solar efficiency
    col1, col2, col3 = st.columns(3, gap="medium")

    col1.markdown("### Solar Efficiency")
    col1.markdown("The ratio between the energy produced by the solar panels and the energy received by the sun.")
    col1.markdown("It is computed as follows:")
    col1.latex(r'''
                \eta = \frac{E_{panels}}{E_{sun}}
                ''')
    
    col2.markdown("### Amount of Energy Produced")
    col2.markdown("A function of the solar efficiency and the energy received by the sun.")
    col2.markdown("It is computed as follows:")
    col2.latex(r'''
                E_{panels} = \eta \times E_{sun}
                ''')
    
    col3.markdown("### Details")
    # list the location, area (m^2), sun radiation (kwh/m^2), solar efficiency (0-10), and amount of electric potential (kwh)
    col3.markdown("📍 Location: "+str(location.address))
    col3.markdown("📐 Area: 38 m^2")
    col3.markdown("☀️ Sun radiation: 1211 kwh/m^2")
    col3.markdown("🌱 Solar efficiency: 4.2/10")
    col3.markdown("⚡ Electric potential: 118 kwh")

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