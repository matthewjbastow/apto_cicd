import sys
import requests
import json

def get_jwt_token(username, password):
    """
    Retrieves a JWT token from the Splunk API.

    :param username: Splunk.com username
    :param password: Splunk.com password
    :return: JWT token if successful, exits otherwise
    """
    auth_url = "https://api.splunk.com/2.0/rest/login/splunk"
    headers = {
        "Content-Type": "application/json"
    }

    # Payload for the POST request with the credentials
    payload = {
        "username": username,
        "password": password
    }

    # Send POST request to Splunk API to get the JWT token
    response = requests.post(auth_url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        # Success - retrieve and return the token
        token = response.json().get('data').get('token')
        if token:
            print(f"Successfully retrieved JWT token: {token}")
            return token
        else:
            print("Error: No token found in the response.")
            sys.exit(1)
    else:
        # Error handling
        print(f"Failed to retrieve JWT token: {response.status_code} {response.text}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python get_jwt_token.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    jwt_token = get_jwt_token(username, password)
    print(f"Retrieved JWT token: {jwt_token}")
