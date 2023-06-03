import requests

api_key = '4b6437820089d8b5502b9c87069a9ddd'


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_value = 8 * forecast_days
    filtered_data = filtered_data[:nr_value]
    return filtered_data


if __name__ == "__main__" :
    print(get_data(place="london", forecast_days=3))
