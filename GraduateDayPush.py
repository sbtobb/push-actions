import sys
from datetime import date
from wxpusher import WxPusher
import requests

def getAllSubscriber(appToken):
    jsonData = WxPusher.query_user('1', '50', appToken)
    uidList = []
    for record in jsonData['data']['records']:
        uidList.append(record['uid'])
    return uidList

def calcDays():
    if date.today() >  date(date.today().year,12,21):
        return (date(date.today().year + 1,12,21) - date.today()).days
    else:
        return (date(date.today().year,12,21) - date.today()).days
    
def getMsg():
    days = calcDays()
    icon = "💪"
    msg = icon + "今天距离考研还有" + str(days) + "天"
    return msg

def wxpush(token,content):
    subscriberList = getAllSubscriber(token)
    result = WxPusher.send_message(content=content,token=token,uids=subscriberList)
    return result

def barkPush(token,title,content):
    r = requests.get('https://api.day.app/'+token+'/'+title+'/'+content)
    return r.json
    
def main():
    APP_TOKEN = sys.argv[1]
    APP_TOKEN2 = sys.argv[2]
    result = barkPush(APP_TOKEN,'考研倒计时',getMsg())
    result = barkPush(APP_TOKEN2,'考研倒计时',getMsg())
    print(result)

if __name__ == "__main__":
    main()
