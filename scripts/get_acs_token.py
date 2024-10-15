import sys
import requests
from requests.auth import HTTPBasicAuth

def get_acs_token(username, password, cloud_url):
    """
    This function retrieves an ACS (App Configuration Service) token
    from Splunk Cloud for further use in ACS API requests.

    :param username: ACS username (either admin username or API key)
    :param password: ACS password (or token associated with the username)
    :param cloud_url: The base URL of the Splunk Cloud instance (e.g., "https://<your-instance>.cloud.splunk.com")
    :return: The ACS token if successful, otherwise exits with an error message
    """
    auth_url = cloud_url

    # Create an HTTP Basic authentication object
    auth = HTTPBasicAuth(username, password)

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(auth_url, auth=auth, headers=headers)

    if response.status_code == 200:
        # Token retrieval successful
        token = response.json().get("token")
        if token:
            print(f"Successfully retrieved ACS token: {token}")
            return token
        else:
            print("Error: No token found in the response.")
            sys.exit(1)
    else:
        # Error during token retrieval
        print(f"Failed to retrieve ACS token: {response.status_code} {response.text}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python get_acs_token.py <username> <password> <cloud_url>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    cloud_url = sys.argv[3]

    token = get_acs_token(username, password, cloud_url)
    print(f"Retrieved ACS token: {token}")
