from flask import Flask
from flask_googlemaps import GoogleMaps

app = Flask(__name__)

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyBGb6HhXgZvkRr8ZI2I5gJYFzkpwpYGG0A"

# Initialize the extension
GoogleMaps(app)

# you can also pass the key here if you prefer
GoogleMaps(app, key="AIzaSyBGb6HhXgZvkRr8ZI2I5gJYFzkpwpYGG0A")

