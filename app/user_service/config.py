from pymongo import MongoClient
import certifi

client = MongoClient('', tlsCAFile=certifi.where())
db = client['SuperTrader']

class Config:
    SECRET_KEY = 'your_secret_key_here'
    JWT_SECRET_KEY = 'your_jwt_secret_key_here'