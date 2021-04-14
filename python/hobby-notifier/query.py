from reddit_oath import *

headers = authenticate()
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get("https://oauth.reddit.com/r/ComblocMarket/hot",
                headers=headers)
for post in res.json()['data']['children']:
        print(post['data']['title'])
        
#print(authenticate())