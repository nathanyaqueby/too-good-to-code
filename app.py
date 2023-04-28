import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide",
                     page_title="Too Good To Code",
                        page_icon="😎",
                        initial_sidebar_state="expanded",
                        menu_items={
                            'Get Help': 'https://www.github.com/nathanyaqueby/too-good-to-code',
                            'Report a bug': "https://www.github.com/nathanyaqueby/too-good-to-code/issues",
                            'About': "# Welcome to Too Good To Code!"
                        })

st.title("Too Good To Code")
# st.markdown("## Welcome to Too Good To Code!")

