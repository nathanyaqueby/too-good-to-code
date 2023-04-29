import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(layout="wide",
                        page_title="Nerd Stats",
                        page_icon="🥸",
                        initial_sidebar_state="expanded"
                        )

st.sidebar.image("img/too good to code.png", use_column_width=True)

st.title("Genistat's Solar Challenge")

# create 3x3 grid layout
col1, col2, col3 = st.beta_columns(3)

with col1:
    st.image("img/solar/1.png", use_column_width=True)

    st.subheader("How many German roofs must be equipped with solar panels to substitute all of Germany's fossil energy sources?")

    st.markdown("""
    Add some text here
    """)

    st.info("""
        The total energy consumption of Germany in 2019 was 2,640 TWh.
        """)

with col2:
    st.image("img/solar/5.png", use_column_width=True)

    st.subheader("In which German regions should solar be subsidized the most?")

    st.markdown("""
    Add some text here
    """)

    st.info("""
        Sources of data:
        - [Solar Atlas](https://www.solaratlas.de/)
        - [Open Power System Data](https://data.open-power-system-data.org/time_series/)
        """)
    
with col3:
    st.image("img/solar/6.png", use_column_width=True)

    st.subheader("Where are the 100 buildings in Germany with the largest roofs and the best efficiency per square meter?")

    st.markdown("""
    Add some text here
    """)

    st.info("""
        And some more text here ...
        """)

st.markdown("---")

