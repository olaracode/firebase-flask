from firebase_admin import credentials, initialize_app, firestore, storage

cred = credentials.Certificate("firebase.json")
default_app = initialize_app(
    cred,
    {
        "storageBucket": "spotify-20df8.appspot.com",
    },
)

firebase_db = firestore.client()
bucket = storage.bucket()
