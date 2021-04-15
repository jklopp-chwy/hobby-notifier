import requests
import config

def authenticate():
        auth = requests.auth.HTTPBasicAuth(config.auth["access_key"], config.auth["secret_key"])
        data = {'grant_type': 'password',
                'username': config.auth["username"],
                'password': config.auth["password"]}

        #bot info
        headers = {'User-Agent': 'Hobby-Notifier/0.0.1'}

        res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
        TOKEN = res.json()['access_token']
        headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

        return(headers)

print(authenticate())