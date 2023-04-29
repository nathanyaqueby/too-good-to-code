import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.mention import mention
import pandas as pd
import numpy as np
import pydeck as pdk
import ee
import geemap.foliumap as geemap
import geopandas as gpd

st.set_page_config(layout="wide",
                        page_title="Panel Detection",
                        page_icon="🏠",
                        initial_sidebar_state="expanded"
                        )

st.markdown("""
    <style>
    .css-8hkptd {
            margin-right: 15px;
        }
    </style>""", unsafe_allow_html=True)

st.title("Genistat's Solar Challenge")
# st.markdown("## Welcome to Too Good To Code!")

@st.cache(persist=True)
def ee_authenticate(token_name="EARTHENGINE_TOKEN"):
    geemap.ee_initialize(token_name=token_name)

@st.cache_data
def read_data(url):
    return gpd.read_file(url)


countries = 'https://github.com/giswqs/geemap/raw/master/examples/data/countries.geojson'
states = 'https://github.com/giswqs/geemap/raw/master/examples/data/us_states.json'

countries_gdf = read_data(countries)
states_gdf = read_data(states)

country_names = countries_gdf['NAME'].values.tolist()
country_names.remove('United States of America')
country_names.append('USA')
country_names.sort()
country_names = [name.replace('.', '').replace(' ', '_')
                 for name in country_names]

state_names = states_gdf['name'].values.tolist()

basemaps = list(geemap.basemaps)

Map = geemap.Map()

with st.sidebar.form(key='my_form'):
    st.title("Initialize the map")

    st.info("""
            Visualize the rooftops on the selected location.
            """)

    basemap = st.selectbox("Select a basemap", basemaps,
                           index=basemaps.index('HYBRID'))
    Map.add_basemap(basemap)

    country = st.selectbox('Select a country', country_names,
                           index=country_names.index('Germany'))

    if country == 'USA':
        state = st.selectbox('Select a city', state_names,
                             index=state_names.index('Munich'))
        layer_name = state

        try:
            fc = ee.FeatureCollection(
                f'projects/sat-io/open-datasets/MSBuildings/US/{state}')
        except:
            st.error('No data available for the selected state.')

    else:
        try:
            fc = ee.FeatureCollection(
                f'projects/sat-io/open-datasets/MSBuildings/{country}')
        except:
            st.error('No data available for the selected country.')

        layer_name = country

    color = st.color_picker('Select a color', '#FF5500')

    style = {'fillColor': '00000000', 'color': color}

    split = st.checkbox("Split-panel map")

    if split:
        left = geemap.ee_tile_layer(fc.style(**style), {}, 'Left')
        right = left
        Map.split_map(left, right)
    else:
        Map.addLayer(fc.style(**style), {}, layer_name)

    Map.centerObject(fc.first(), zoom=16)

    # with st.expander("Data Sources"):
    #     st.info(
    #         """
    #         [Microsoft Building Footprints](https://gee-community-catalog.org/projects/msbuildings/)
    #         """
    #     )
    
    if st.form_submit_button("Initialize", type="primary", use_container_width=True):
        st.write("Initialized!")

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

Map.to_streamlit(height=700)