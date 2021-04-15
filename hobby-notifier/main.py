from reddit_auth import *
from twilio_auth import *
import config

#set keywords
keywords = "WTB"

#vars
client = Client(account_sid, auth_token)
queryList = []
headers = authenticate()

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get(config.hobby["subreddit"],
                headers=headers)
for post in res.json()['data']['children']:
        queryList.append((post['data']['title']))

#search the above list for the keyword and generate a new list. searching substring within a string. https://www.w3schools.com/python/python_lists_comprehension.asp
dataList = [x for x in queryList if keywords in x]


count = 0
for title in dataList:
        message = client.messages.create(
                to=my_phone_number, 
                from_=sending_number,
                body=dataList[count])
        print(message.sid)
        count = count +1