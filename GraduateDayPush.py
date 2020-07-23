import sys
from datetime import date
import requests

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


def barkPush(token,title,content):
    r = requests.get('https://api.day.app/'+token+'/'+title+'/'+content)
    return r.text
    
def main():
    APP_TOKEN = sys.argv[1]
    APP_TOKEN2 = sys.argv[2]
    result = barkPush(APP_TOKEN,'考研倒计时',getMsg())
    result = barkPush(APP_TOKEN2,'考研倒计时',getMsg())
    print(result)

if __name__ == "__main__":
    main()
