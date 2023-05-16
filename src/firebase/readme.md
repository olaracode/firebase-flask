# first steps

To start using firebase in your application the first thing you need to do is create a firebase application and create a storage bucket and finally generate a service account key to manage your bucket(This will download a .json file that we'll need later)

Once you have the key the next step is add it to the firebase folder, and add this to your Pipfile scripts

```.env
firebase = "python your/route/firebase/firebase_scripts.py"
```

Then run pipenv run firebase, this should add the necesary keys to your .env file
