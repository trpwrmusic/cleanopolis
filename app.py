import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import st_folium
import folium


st.title('Cleanopolis')

st.subheader('Map of pollution')

# center on Liberty Belt, add marker
m = folium.Map(location = [39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282],
    popup="Bell",
    tooltip="Bell"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width = 725)


picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)