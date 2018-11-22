import firebase_admin
import datetime
from firebase_admin import credentials, firestore

cred = credentials.Certificate("vehicleplaterecognition-private-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def add_plate_to_firebase(plateId):
    db.collection('found-plates').add({
        'plateId': plateId,
        'timestamp': datetime.datetime.now()
    })
    print('added plate id to firebase')

add_plate_to_firebase('VDZ-678')

