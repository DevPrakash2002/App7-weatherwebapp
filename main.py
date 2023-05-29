import streamlit as st

st.title("Weather forecast for Day")

place = st.text_input("Place")
date = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the no forecast Days")

option = st.selectbox("Select Data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for next {date} Days in {place}")