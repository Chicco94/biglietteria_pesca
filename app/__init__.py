from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.static_folder = 'static'
path = "app/files/biglietti.txt"

from app import routes, models

if __name__=="__main__":
    app.run()

    
# FLASK_APP=main.py FLASK_ENV=development flask run
