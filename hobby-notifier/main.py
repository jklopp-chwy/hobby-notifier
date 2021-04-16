from reddit_auth import *
from twilio_auth import *
import config
import time
import mysql.connector

queryList = []
dataList = []
headers = authenticate()

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
res = requests.get(config.hobby["subreddit"], headers=headers)

for post in res.json()['data']['children']:
        queryList.append(
                (post['data']['title'])
                )

def checkData():
        mycursor = config.mydb.cursor(buffered=True)
        count = 0
        for k in config.keywords:
                for s in queryList:
                        if k in s:
                                mycursor.execute("SELECT count(*) FROM posts WHERE post_id = %(s)s", {'s': s});
                                myresult = mycursor.fetchall()
                                if (myresult == [(0,)]):
                                        print(f"LOGGING....... {s}")
                                        #sendSms(s)
                                        mycursor.execute("INSERT INTO posts (post_ID) VALUES (%(s)s)", {'s': s});
                                        config.mydb.commit()  
        return

checkData()
