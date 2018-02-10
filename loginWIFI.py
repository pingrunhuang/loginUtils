import requests

'''
This script is used for automatically log in to our wifi system
'''

home_url = 'http://192.168.14.118/portal/'
login_url = 'http://192.168.14.118/portal/logon.cgi'

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Host":"192.168.14.118",
    "Referer":home_url,
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

# this is part is really something that should be change according to different website 
# checkout the form data part and include every part in that block to this field
payload = {
    "PtUser": 'runping.huang',
    "PtPwd": '20170605',
    "PtButton": "Logon",
}

session = requests.Session()

response = None
try:
    response = session.get(url=home_url, data=payload, headers=headers)
except requests.exceptions.ConnectionError as error:
    print(error)

headers['Origin']='http://192.168.14.118'
headers['Referer']='http://192.168.14.118/portal/'

response = session.post(url=login_url, data=payload, headers=headers)
print('You have logged in: ', response.status_code)

