from pymongo import MongoClient
import certifi

client = MongoClient('', tlsCAFile=certifi.where())
db = client['SuperTrader']
