from firebase_admin import credentials, initialize_app, firestore, storage
from .firebase_settings import FIREBASE_CONFIG


cred = credentials.Certificate(FIREBASE_CONFIG)
default_app = initialize_app(
    credential=cred,
    options={
        "storageBucket": "spotify-20df8.appspot.com",
    },
)

firebase_db = firestore.client()
firebase_bucket = storage.bucket()


class FirebaseBucket:
    def __init__(self):
        self.bucket = firebase_bucket

    def upload_file(self, file, filename):
        blob = self.bucket.blob(filename)
        blob.upload_from_file(file)
        blob.make_public()
        return blob.public_url

    def delete_file(self, filename):
        blob = self.bucket.blob(filename)
        blob.delete()
        return True


Bucket = FirebaseBucket()
