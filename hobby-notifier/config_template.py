import mysql.connector
auth = {
    "username": "#your reddit bot username",
    "password": "your reddit bot password",
    "access_key": "your app script access key",
    "secret_key": "your app script secret key"
}

#input the subreddit and keyword you want to search for
hobby = {
    "subreddit": "string, the subreddit you want to monitor"
}

keywords = ["dogs, cats, food, fun"]

twilio = {
    "account_sid": "####",
    "auth_token": "#####",
    "twilio_phone_number": "+1#######",
    "my_phone_number": "1#######"
}

mydb = mysql.connector.connect(
  host="####,
  user="###",
  password="####",
  database="posts"
)