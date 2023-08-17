# Weather Application

The Weather Application is a Python script that utilizes the OpenWeatherMap API to retrieve weather data for a 
specified city. The application fetches current temperature, weather description, humidity, and wind speed and 
displays the information in the terminal.
The user can enter the city name to get the weather information, and they can exit the application by 
entering "exit".


## Prerequisites

- Python 3.x
- `requests` library (can be installed using `pip install requests`)

## Getting Started

1. Clone the repository to your local machine:

```shell
git https://github.com/PiusEzekiel/api-weather-app.git
```

2. Navigate to the project directory:

```shell
cd weather-app
```

3. Obtain an API key from OpenWeatherMap:

- Visit the OpenWeatherMap website (https://openweathermap.org/) and sign up for a free account.
- Retrieve your API key from your account dashboard.

4. Open the `weather-app.py` file in a text editor.

1. Replace the value of the `user_api` variable with your OpenWeatherMap API key:

```python
user_api = 'YOUR_API_KEY'
```

6. Save the changes to the `weather-app.py` file.

## Usage

1. In a terminal, navigate to the project directory.

1. Run the script using the following command:

```shell
python3 weather-app.py
```

3. Enter the name of the city for which you want to retrieve weather information when prompted.

1. The script will fetch the weather data from the OpenWeatherMap API and display the following information in the terminal:

- Current temperature in degrees Celsius
- Current weather description
- Current humidity percentage
- Current wind speed in kilometers per hour

## Demo

Please watch the following 2-minute video demonstrating how to use the Weather Application: https://shorturl.at/luyB2

## Credits

The Weather Application utilizes the OpenWeatherMap API, and credit is given to the API developer for providing the weather data.

- OpenWeatherMap API: https://home.openweathermap.org/

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Weather Application was developed as part of a learning experience.
- The application demonstrates the use of APIs to fetch and display weather data.

## Contact

If you have any questions or feedback, please contact Pius at e.pius@alustudent.com
