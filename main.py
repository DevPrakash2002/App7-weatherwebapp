import streamlit as st
import plotly.express as px

st.title("Weather forecast for Day")

place = st.text_input("Place")
date = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the no forecast Days")

option = st.selectbox("Select Data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for next {date} Days in {place}")

dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
temperature = [10, 11, 15]

figure = px.line(x=dates, y=temperature, labels={'x': "Date", 'y': "Temperature"})
st.plotly_chart(figure)