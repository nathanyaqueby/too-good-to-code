import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide",
                        page_title="Regions and Clusters",
                        page_icon="🗺️",
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

m = leafmap.Map(center=[40, -100], zoom=4)
cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.csv'
regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.geojson'

m.add_geojson(regions, layer_name='US Regions')
m.add_points_from_xy(
    cities,
    x="longitude",
    y="latitude",
    color_column='region',
    icon_names=['gear', 'map', 'leaf', 'globe'],
    spin=True,
    add_legend=True,
)