from reddit_auth import *
from twilio_auth import *
import config

client = Client(account_sid, auth_token)
queryList = []
dataList = []
keywords = []
headers = authenticate()
keywords = config.keywordsConfig

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get(config.hobby["subreddit"],
                headers=headers)
for post in res.json()['data']['children']:
        queryList.append((post['data']['title']))

def checkData():
    count = 0
    for k in keywords:
        for s in queryList:
                if k in s:
                        print(s)
                        sendSms(s)

checkData()