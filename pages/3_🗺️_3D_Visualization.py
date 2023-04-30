import streamlit as st
from streamlit.components.v1 import components
from streamlit_extras.mention import mention
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide",
                        page_title="3D Visualizations",
                        page_icon="🗺️",
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

# with st.sidebar.form(key='my_form'):
#     st.title("Initialize the map")

#     st.info("""
#             For the given location, 
#             we have to find out how many solar panels can we fit and 
#             how much energy can they produce.
#             """)

#     country_names = pd.read_csv("data/average-latitude-longitude-countries.csv")["Country"].values.tolist()

#     # set up a dropdown menu to select the country of interest
#     country = st.selectbox("Select a country", country_names, index=country_names.index('Germany'))

#     # set up a slider to select the number of panels
#     num_panels = st.slider("Select the number of panels", 0, 100, 50)

#     # set up a slider to filter the efficiency
#     efficiency = st.slider("Select the efficiency", 0.0, 1.0, 0.5, 0.01)

#     # add radio buttons to show the raster or the vector map
#     map_type = st.radio("Select the map type", ("Raster", "Vector"), horizontal=True)

#     # create a submit button to retrain the model
#     if st.form_submit_button("Generate visualization", type="primary", use_container_width=True):
#         st.write("Done!")

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

# # set a progress bar
# progress_text = "Loading the map..."
# my_bar = st.progress(0, progress_text)

# m = leafmap.Map(center=[40, -100], zoom=4)
# cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.csv'
# regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.geojson'

# progress_text = "Almost there..."
# my_bar.progress(50, progress_text)

# m.add_geojson(regions, layer_name='Munich')
# m.add_points_from_xy(
#     cities,
#     x="longitude",
#     y="latitude",
#     # color_column='region',
#     icon_names=['gear', 'map', 'leaf', 'globe'],
#     spin=True,
#     add_legend=True,
# )

# my_bar.progress(80, progress_text)

# m.to_streamlit(height=700, bidirectional=True)

# progress_text = "Finished!"
# my_bar.progress(100, progress_text)