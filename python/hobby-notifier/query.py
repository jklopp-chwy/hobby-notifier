from reddit_oath import *
import config

#set keywords
keywords = "Russian"

#vars
queryList = []
headers = authenticate()

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get(config.hobby["subreddit"],
                headers=headers)
for post in res.json()['data']['children']:
        queryList.append((post['data']['title']))

#search the above list for the keyword and generate a new list. searching substring within a string
dataList = [str for str in queryList if keywords in str]
print(dataList)