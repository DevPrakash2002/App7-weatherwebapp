import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for Day")

place = st.text_input("Place")
day = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the no forecast Days")

option = st.selectbox("Select Data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for next {day} Days in {place}")

data = get_data(place, day, option)

figure = px.line(x=d, y=t, labels={'x': "Date", 'y': "Temperature"})
st.plotly_chart(figure)