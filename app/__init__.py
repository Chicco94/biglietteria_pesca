from flask import Flask
from config import Config
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Config)
db = open("files/biglietti.txt")

from app import routes, models