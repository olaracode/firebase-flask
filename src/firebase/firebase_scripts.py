import json

"""
This file has a script that extends the current .env file with the contents of the firebase.json - Your firebase - file. You should also add the firebase.json file to your .gitignore file to prevent leaking private keys.
"""

with open("src/firebase/firebase.json", "r") as f:
    service_account = json.load(f)
    env_str = f"""\
TYPE={service_account['type']}
PROJECT_ID={service_account['project_id']}
PRIVATE_KEY_ID={service_account['private_key_id']}
PRIVATE_KEY=\"{service_account['private_key']}\"
CLIENT_EMAIL={service_account['client_email']}
CLIENT_ID={service_account['client_id']}
AUTH_URI={service_account['auth_uri']}
TOKEN_URI={service_account['token_uri']}
AUTH_PROVIDER_CERT_URL={service_account['auth_provider_x509_cert_url']}
CLIENT_CERT_URL={service_account['client_x509_cert_url']}\
"""


# open and add at the end of the file
with open(".env", "a") as f:
    f.write(env_str)
