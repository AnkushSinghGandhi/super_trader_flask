from pymongo import MongoClient
import certifi

client = MongoClient('mongodb+srv://manthangehlot66:rahulsharma@optionaro.f2tgbib.mongodb.net/?retryWrites=true&w=majority&appName=OptionARO', tlsCAFile=certifi.where())
db = client['OptionARO']