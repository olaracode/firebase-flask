import json

with open("firebase.json", "r") as f:
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

print(env_str)

# f.write(env_str)
