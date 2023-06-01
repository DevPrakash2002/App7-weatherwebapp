import streamlit as st
import plotly.express as px

st.title("Weather forecast for Day")

place = st.text_input("Place")
date = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the no forecast Days")

option = st.selectbox("Select Data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for next {date} Days in {place}")
def get_data(date):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [date * i for i in temperatures]
    return dates, temperatures

d, t = get_data(date)

figure = px.line(x=d, y=t, labels={'x': "Date", 'y': "Temperature"})
st.plotly_chart(figure)