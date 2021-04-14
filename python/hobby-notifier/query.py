from reddit_oath import *
import re

#set keywords
keywords = ["russian"]

#vars
queryList = []
dataList = []
headers = authenticate()

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get("https://oauth.reddit.com/r/ComblocMarket/new",
                headers=headers)
for post in res.json()['data']['children']:
        queryList.append((post['data']['title']))

print(queryList)

#results = [x for x in queryList if all(re.search("\\b{}\\b".format(w), x) for w in keywords)]

#print(results)

if '[WTB] Romy Palmswell HG’s - $40 +/- [VA]' in queryList:
        print("test")