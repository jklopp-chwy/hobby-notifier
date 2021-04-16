from reddit_auth import *
from twilio_auth import *
import config
import time
import mysql.connector

client = Client(account_sid, auth_token)
queryList = []
dataList = []
keywords = []
headers = authenticate()
#keywords = config.keywordsConfig

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
res = requests.get(config.hobby["subreddit"], headers=headers)

for post in res.json()['data']['children']:
        queryList.append(
                (post['data']['title'])
                )

#print(queryList)

def checkData():
        mycursor = config.mydb.cursor(buffered=True)
        count = 0
        for k in config.keywords:
                for s in queryList:
                        if k in s:
                                temp = """SELECT COUNT(*) from posts where post_id = (("%s"))""" % (s)
                                mycursor.execute(temp)
                                myresult = mycursor.fetchall()
                                print(myresult)
                                if (myresult == [(0,)]):
                                        print(f"logging {s}")
                                        sendSms(s)
                                        sql = """INSERT INTO posts (post_ID) VALUES (("%s"))"""  % (s)
                                        mycursor.execute(sql)
                                        config.mydb.commit()
                                
        return

checkData()
