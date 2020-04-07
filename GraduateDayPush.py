import sys
from datetime import date
from wxpusher import WxPusher

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
    
def main():
    APP_TOKEN = sys.argv[1]
    subscriberList = getAllSubscriber(APP_TOKEN)
    msg = getMsg()
    result = WxPusher.send_message(content=msg,token=APP_TOKEN,uids=subscriberList)
    print(result)

if __name__ == "__main__":
    main()