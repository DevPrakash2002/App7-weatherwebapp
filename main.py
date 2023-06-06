import streamlit as st
import plotly.express as px
from backend import get_data
# Adding title, select-box, slider and sub-headers
st.title("Weather forecast for Day")

place = st.text_input("Place")
day = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the no forecast Days")

option = st.selectbox("Select Data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for next {day} Days in {place}")
# Get the Temperature or Sky Data
try:
    if place:
        filtered_data = get_data(place=place, forecast_days=day)
    # plotting the graph and displaying temperature data received
    if option == "Temperature":
        temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
        date = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=date, y=(temperatures), labels={'x': "Date", 'y': "Temperature"})
        st.plotly_chart(figure)

    # displaying sky data
    if option == "Sky":
        temperatures = [dict["weather"][0]["main"] for dict in filtered_data]
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
        image_path = [images[condition] for condition in temperatures]
        st.image(image_path, width=112)

except KeyError:
    st.text("PLease enter a valid place")
