from reddit_oath import *
import config

#set keywords
keywords = "AKM"

#vars
queryList = []
dataList = []
headers = authenticate()

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get(config.hobby["subreddit"],
                headers=headers)
for post in res.json()['data']['children']:
        queryList.append((post['data']['title']))

#print(queryList)

l1 = [title for title in queryList if keywords in title]

print(l1)