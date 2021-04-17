# Hobby Notifier v 0.1.1

This python bot automatically searches your favorite subreddit for specified keywords. If a keyword is found, it will notify you via SMS, so you have a better chance of buying/selling/trading goods for your favorite hobby! I personally enjoy r/hardwareswap/, r/ComblocMarket/, r/GearTrade/, and a few others. Hope you enjoy!
------------
## APIs Used:

- https://www.reddit.com/dev/api
- https://www.twilio.com/docs/sms

## Documentation that was useful in building:
- https://martin-thoma.com/configuration-files-in-python/
- https://markdown-editor.github.io/


------------

## Prerequisites

1. running mysql instance, I prefer [AWS RDS](https://aws.amazon.com/rds/ "AWS RDS")

2. create database
```sql
CREATE DATABASE posts;
use posts;
```
3. create table structure
```sql
CREATE TABLE posts (
	 id INT NOT NULL AUTO_INCREMENT,
	post_id varchar(500)
);
```
4. Twilio account: https://www.twilio.com/try-twilio (use my referal code for extra credits www.twilio.com/referral/KkGYmq)
5. Reddit account, then register your bot app for the reddit API credentials: https://www.reddit.com/prefs/apps/

## Running automatically on EC2/RDS

1. Launch an EC2 ubuntu AMI
2. SSH onto server
3. sudo apt-get update
4. sudo apt-get install python3-venv
5. sudo apt-get upgrade
3. git clone https://github.com/jklopp/hobby-notifier
4. create and input values in config.py nano  hobby-notifier/hobby-notifier/config.py
4. python3 -m venv hobby-notifier/hobby-notifier/venv
5. source hobby-notifier/hobby-notifier/venv/bin/activate
6. pip3 install -r hobby-notifier/requirements.txt 
7. crontab -e


```bash
SHELL=/bin/bash
* * * * * source /home/ubuntu/hobby-notifier/hobby-notifier/venv/bin/activate && python3 /home/ubuntu/hobby-notifier/hobby-notifier/main.py >> /home/ubuntu/hobby-notifier/logs/log.txt
```