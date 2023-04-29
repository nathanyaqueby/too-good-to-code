import streamlit as st
import streamlit.components.v1 as components
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

st.title("Genistat's Solar Challenge")
# st.markdown("## Welcome to Too Good To Code!")

with st.sidebar.form(key='my_form'):
    st.title("Initialize the map")

    st.info("""
                    For the given location, 
                    we have to find out how many solar panels can we fit and 
                    how much energy can they produce.
                """, icon="🗒️")

    country_names = pd.read_csv("data/average-latitude-longitude-countries.csv")["Country"].values.tolist()

    # set up a dropdown menu to select the country of interest
    country = st.selectbox("Select a country", country_names, index=country_names.index('Germany'))

    # set up a slider to select the number of panels
    num_panels = st.slider("Select the number of panels", 0, 100, 50)

    # set up a slider to filter the efficiency
    efficiency = st.slider("Select the efficiency", 0.0, 1.0, 0.5, 0.01)

    # add radio buttons to show the raster or the vector map
    map_type = st.radio("Select the map type", ("Raster", "Vector"), horizontal=True)

    # create a submit button to retrain the model
    if st.form_submit_button("Generate visualization", type="primary", use_container_width=True):
        st.write("Done!")

with st.sidebar.form(key='download'):
    st.title("Solar Efficiency Report")

    st.markdown("Save all the results of the solar efficiency analysis and the visualizations in a PDF file.")

    # create a submit button to download the retrained model
    if st.form_submit_button("Download as PDF", type="secondary", use_container_width=True):
        st.write("Downloaded!")

st.sidebar.markdown("---")
st.sidebar.markdown("Read more about the project on [GitHub](www.github.com/nathanyaqueby/too-good-to-code).")

@st.cache(persist=True)
def ee_authenticate(token_name="EARTHENGINE_TOKEN"):
    geemap.ee_initialize(token_name=token_name)


col1, col2 = st.columns([8, 2])


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

with col2:

    basemap = st.selectbox("Select a basemap", basemaps,
                           index=basemaps.index('HYBRID'))
    Map.add_basemap(basemap)

    country = st.selectbox('Select a country', country_names,
                           index=country_names.index('USA'))

    if country == 'USA':
        state = st.selectbox('Select a state', state_names,
                             index=state_names.index('Florida'))
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

    with st.expander("Data Sources"):
        st.info(
            """
            [Microsoft Building Footprints](https://gee-community-catalog.org/projects/msbuildings/)
            """
        )


with col1:

    Map.to_streamlit(height=1000)