import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]

# 填写server酱sckey,不开启server酱则不用填
sckey = os.environ["SCKEY"]

# 填入glados账号对应cookie
cookie = os.environ["COOKIE"]

cookie2 = os.environ["COOKIE2"]

def start2():    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin2 = requests.post(url,headers={'cookie2': cookie2 ,'referer': referer })
    state2 =  requests.get(url2,headers={'cookie2': cookie2 ,'referer': referer})

    if 'message2' in checkin.text:
        mess2 = checkin2.json()['message']
        time2 = state2.json()['data']['leftDays']
        time2 = time2.split('.')[0]
        print(time2)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess2+'，you have '+time2+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start2()

if __name__ == '__main__':
    start2()

    
