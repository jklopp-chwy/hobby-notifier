from reddit_oath import *
import config

#set keywords
keywords = ["russian"]

#vars
queryList = []
dataList = []
headers = authenticate()

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get(config.hobby["subreddit"],
                headers=headers)
for post in res.json()['data']['children']:
        queryList.append((post['data']['title']))

print(queryList)

#if '[WTB] Romy Palmswell HG’s - $40 +/- [VA]' in queryList:
        #print("test")