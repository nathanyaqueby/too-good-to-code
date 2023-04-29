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

st.title("Genistat's Solar Challenge")

# create 3x3 grid layout
col1, col2, col3 = st.beta_columns(3)

with col1:
    st.image("img/solar/1.png", use_column_width=True)

    st.subheader("How many German roofs must be equipped with solar panels to substitute all of Germany's fossil energy sources?")

    st.info("""
        The total energy consumption of Germany in 2019 was 2,640 TWh.
        """)