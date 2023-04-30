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
    According to [sources](https://www.destatis.de/EN/Themes/Economic-Sectors-Enterprises/Energy/Production/_node.html), among the 571.3 billion kWh produced, 44% are renewables while 56% are conventional.
     This means that we have 319.928 billion kWh to substitute for, spread across 22.562.032 average houses in Germany.
    """)

    # st.info("""
    #     Insert answer here
    #     """)

with col2:
    st.image("img/solar/5.png", use_column_width=True)

    st.subheader("In which German regions should solar be subsidized the most?")

    st.markdown("""
    After calculating the region with the most amount of sun radiation and the most amount of roofs, we conclude that the region of Berlin should be subsidized the most.
    """)

    # st.info("""
    #     Sources of data:
    #     - [Solar Atlas](https://www.solaratlas.de/)
    #     - [Open Power System Data](https://data.open-power-system-data.org/time_series/)
    #     """)
    
with col3:
    st.image("img/solar/6.png", use_column_width=True)

    st.subheader("Where are the 100 buildings in Germany with the largest roofs and the best efficiency per square meter?")

    st.markdown("""
    Sorting the top 100 buildings by roof size and efficiency per square meter in the datasets of Hamburg, Berlin, and Bremen, we conclude that Bremen has the most efficient buildings in average.
    """)

    # st.info("""
    #     And some more text here ...
    #     """)

st.markdown("---")

