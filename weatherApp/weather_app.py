import requests
from flask import Flask, request, render_template
import config

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        city, temperature = get_temperature()
        return f"<p>The current temperature in {city} is {temperature}°C.</p>"
    else:
        return render_template("index.html")
    
def get_temperature():
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        return(city, temperature)


if __name__ == "__main__":
    app.run(debug=True)