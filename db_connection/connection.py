from pymongo import MongoClient
import pprint

client = MongoClient()

client = MongoClient('localhost', 27017)

db = client.biglietteria

biglietti = db.biglietti

biglietto = {
    'numero': 1
}

#biglietto_id = biglietti.insert_one(biglietto).inserted_id

#print(biglietto_id)

pprint.pprint(biglietti.find_one())

client.close()