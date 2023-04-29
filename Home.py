import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import pydeck as pdk

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

# ## base python libraries
# from typing import cast

# ## pip installed libraries
# import folium
# import streamlit as st
# from streamlit_folium import st_folium

# ## repo-local code
# from constants import COLUMN_VALS
# from coordinates import Coordinates
# from sfdb import sfconn, get_feature_collection, state_capitals, get_fld_values
# from utils import add_data_to_map, get_order, get_capital_data

# ## TODO: how do we get this off this page?
# ## Don't know how to pass arguments in callbacks
# def clear_state():
#     del st.session_state[autostate]


# ## connect to snowflake
# conn = sfconn(**st.secrets["sfdevrel"])

# ## put sidebar widgets up as high as possible in code to avoid flickering
# ## pick OSM table, tables organized by geo data type
# tbl = st.sidebar.selectbox(
#     "1. Choose a geometry type",
#     ["Point", "Line", "Polygon"],
#     key="table",
# )

# ## from tbl chosen, get the relevant columns
# col_selected = st.sidebar.selectbox(
#     "2. Choose a column",
#     COLUMN_VALS[tbl.lower()],
#     key="col_selected",
# )

# ## for a given relevant column, pick tags you want to plot
# tgs = get_fld_values(conn, tbl, col_selected)
# tags = st.sidebar.multiselect(
#     "3. Choose tags to visualize",
#     tgs,
#     key="tags",
#     help="Tags listed by frequency high-to-low",
# )

# ## optionally, center map on a capital city
# capitals = ["--NONE--"] + list(state_capitals(conn)["NAME"].values)
# capital = st.sidebar.selectbox(
#     "(Optional) Zoom map to capital?",
#     options=capitals,
#     key="capital",
#     on_change=clear_state,
# )

# ## set row maximum to avoid requesting too much data
# st.sidebar.write("---")  ## visual divider between less important input
# num_rows = st.sidebar.select_slider(
#     "Maximum number of rows",
#     [100, 1000, 10_000, 100_000, 1_000_000],
#     value=1000,
#     key="num_rows",
# )

# ## get key of automatically written state
# ## this is slightly hacky, relies on undocumented Streamlit API
# autostate = cast(str, sorted(st.session_state.keys(), key=get_order)[-1])

# capital_data = get_capital_data(conn, capital)

# ## initialize starting value of zoom if it doesn't exist
# ## otherwise, get it from session_state
# try:
#     zoom = st.session_state[autostate]["zoom"]
# except (TypeError, KeyError):
#     if capital_data is None:
#         zoom = 4
#     else:
#         zoom = capital_data["zoom"]

# ## initialize starting value of center if it doesn't exist
# ## otherwise, get it from session_state
# try:
#     center = st.session_state[autostate]["center"]
# except (TypeError, KeyError):
#     if capital_data is None:
#         center = {"lat": 37.97, "lng": -96.12}
#     else:
#         center = capital_data["center"]

# "### 🗺️ OpenStreetMap - North America"
# "---"

# ## Initialize Folium
# m = folium.Map(location=(center["lat"], center["lng"]), zoom_start=zoom)

# ## defaults prior to map rendering
# try:
#     coordinates = Coordinates.from_dict(st.session_state[autostate]["bounds"])
# except TypeError:
#     coordinates = Coordinates.from_dict(
#         {
#             "_southWest": {"lat": 10.31491928581316, "lng": -140.09765625000003},
#             "_northEast": {"lat": 58.17070248348609, "lng": -52.20703125000001},
#         }
#     )

# ## get geo data from Snowflake
# st.session_state["features"] = get_feature_collection(
#     conn, coordinates, column=col_selected, table=tbl, num_rows=num_rows, tags=tags
# )

# ## add geo data to `m` Folium object
# add_data_to_map(
#     col_selected, st.session_state["features"], m, table=tbl, column=col_selected
# )

# ## display Folium map in Streamlit
# map_data = st_folium(m, width=1000)

# sidebar   
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