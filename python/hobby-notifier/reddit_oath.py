import requests


def authenticate():
        auth = requests.auth.HTTPBasicAuth('XL7-X887Y2zB1Q', 'IPRlpCtEJwlpZpVgXX5bn2cMti_-2Q')

        data = {'grant_type': 'password',
                'username': 'Hobby-notifier-bot',
                'password': 'BmakGkFNsptnuM8c'}

        #bot info
        headers = {'User-Agent': 'Hobby-Notifier/0.0.1'}

        #get oauth token using auth, data, and headers
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

        TOKEN = res.json()['access_token']

        # add authorization to our headers dictionary
        headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

        return(headers)