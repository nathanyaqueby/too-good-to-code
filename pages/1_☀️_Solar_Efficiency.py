import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import pydeck as pdk

############ add logo
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: "img/too good to code.png";
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()

st.set_page_config(layout="wide",
                        page_title="Solar Efficiency",
                        page_icon="☀️",
                        initial_sidebar_state="expanded"
                        )

st.title("Genistat's Solar Challenge")
# st.markdown("## Welcome to Too Good To Code!")

############# function to create the map
def create_map(radius, city):

    # get the latitude and longitude of the city
    lat = data["lat"].loc[data["city"] == city].values[0]
    lon = data["lng"].loc[data["city"] == city].values[0]

    chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [lat, lon],
    columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=lat,
            longitude=lon,
            zoom=11,
            pitch=50,
            height=700,
        ),
        layers=[
            pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[lon, lat]',
            radius=radius,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=radius,
            ),
        ],
    ), use_container_width=True)

with st.sidebar.form(key='my_form'):
    st.title("Initialize the map")

    st.info("""
                For the given location, 
                we have to find out how many solar panels can we fit and 
                how much energy can they produce.
            """, icon="🗒️")
    
    data = pd.read_csv("data/simplemaps_worldcities_basicv1.76/worldcities.csv")

    # get the unique country names
    country_names = data["country"].unique().tolist()

    # set up a dropdown menu to select the country of interest
    country = st.selectbox("Select a country", country_names, index=country_names.index('Germany'))

    # set a dropdown menu with cities according to the country selected
    city_names = data["city"].loc[data["country"] == country].unique().tolist()
    city = st.selectbox("Select a city", city_names, index=city_names.index('Munich'))

    # set up a slider to select the number of panels
    radius = st.slider("Select the radius", 0, 500, 200)

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

create_map(radius, city)