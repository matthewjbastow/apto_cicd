import sys
import requests

def submit_to_appinspect_api(app_package, jwt_token):
    url = "https://appinspect.splunk.com/v1/app/validate"
    headers = {
        "Authorization": f"bearer {jwt_token}",
        "Content-Type": "application/gzip"
    }
    with open(app_package, 'rb') as f:
        response = requests.post(url, headers=headers, files={'app_package': f})

    if response.status_code == 200:
        result = response.json()
        print("AppInspect API result:", result)
    else:
        print("Error submitting to AppInspect API:", response.status_code)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python inspect_splunk_app_api.py <app_package> <jwt_token>")
        sys.exit(1)

    app_package = sys.argv[1]
    jwt_token = sys.argv[2]
    submit_to_appinspect_api(app_package, jwt_token)