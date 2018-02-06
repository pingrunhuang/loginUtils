import requests 
from bs4 import BeautifulSoup

# how to deal with https?
homeurl = 'http://oa.shijinshi.cn/sjsinfo/main/login'
loginurl = 'http://oa.shijinshi.cn/sjsinfo/main?login'

hostname = 'oa.shijinshi.cn'

headers = {
   "Accept": "text/html, application/xhtml+xml, image/jxr, */*",
   "Accept-Encoding": "gzip, deflate, br",
   "Accept-Language": "en-US, en; q=0.8, zh-Hans-CN; q=0.7, zh-Hans; q=0.5, fr-FR; q=0.3, fr; q=0.2",
   "Connection": "Keep-Alive",
   "Cookie": "sjsinfo.session.id=f7bca64a800449fd91f52ba2157d1199",
   "Host": "oa.shijinshi.cn",
   "Referer": "https://oa.shijinshi.cn/sjsinfo/main",
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
}

payload = {
    'username': 'huangrunping',
    'password': 'qwer1234'
}

session = requests.session()
response = session.post(url=homeurl, data=payload, headers=headers)
print("response code from server is ", response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link)
print("Before login: ", soup.find('a'))
headers['Referer'] = 'http://oa.shijinshi.cn/sjsinfo/main/oa/workClockInRecord/clockInOrOut'
response = session.post(url="http://oa.shijinshi.cn/sjsinfo/main/login", data=payload, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
print("After login:", soup.find('a'))
