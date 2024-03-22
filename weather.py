import requests

def get_weather(city):
    api_key = "4a4027d0cf454ca29ac95522242203"  # Replace with your actual API key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data["current"]["temp_c"]

city = input("Enter the city name: ")
temperature = get_weather(city)
print(f"The temperature in {city} is {temperature}°C")
choice = input("Do you want to check the weather of another city? (yes/no): ")
if choice.lower() == "yes":
    city = input("Enter the city name: ")
    temperature = get_weather(city)
    print(f"The temperature in {city} is {temperature}°C")

def main():
    while True:
        city = "no"
        break

if __name__ == "__main__":
    main()