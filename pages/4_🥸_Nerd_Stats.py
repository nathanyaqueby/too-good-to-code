import streamlit as st
from streamlit_extras.mention import mention

st.set_page_config(layout="wide",
                        page_title="Nerd Stats",
                        page_icon="🥸",
                        initial_sidebar_state="expanded"
                        )

st.markdown("""
    <style>
    .css-8hkptd {
            margin-right: 15px;
        }
    </style>""", unsafe_allow_html=True)

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

# st.sidebar.markdown("---")
# st.sidebar.markdown("Read more about the project on [GitHub](www.github.com/nathanyaqueby/too-good-to-code).")
st.sidebar.image("img/too good to code.png", use_column_width=True)

st.title("Genistat's Solar Challenge")

# create 3x3 grid layout
col1, col2, col3 = st.beta_columns(3, gap="large")

with col1:
    st.image("img/solar/1.png", use_column_width=True)

    st.subheader("How many German roofs must be equipped with solar panels to substitute all of Germany's fossil energy sources?")

    st.markdown("""
    Add some text here
    """)

    st.info("""
        The total energy consumption of Germany in 2019 was 2,640 TWh ([Source](https://www.energy-charts.de/energy_pie.htm?year=2019&source=all-sources&period=annual&week=52&mode=relative&external=cal-external)).
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

