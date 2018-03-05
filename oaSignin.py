import requests 
from bs4 import BeautifulSoup
import logging
import os
import time

# how to deal with https?
homeurl = 'http://oa.shijinshi.cn/sjsinfo/main/login'
loginurl = 'http://oa.shijinshi.cn/sjsinfo/main?login'

# initial logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=os.getcwd()+'/oaSignin.log',
                    filemode='w')
logger = logging.getLogger('loginUtils')
logger.setLevel(logging.INFO)


hostname = 'oa.shijinshi.cn'

headers = {
   "Accept": "text/html, application/xhtml+xml, image/jxr, */*",
   "Accept-Encoding": "gzip, deflate, br",
   "Accept-Language": "en-US, en; q=0.8, zh-Hans-CN; q=0.7, zh-Hans; q=0.5, fr-FR; q=0.3, fr; q=0.2",
   "Connection": "Keep-Alive",
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
if response.status_code==200:
    logger.info(msg="Successfully logged in...")
    headers['Referer'] = 'http://oa.shijinshi.cn/sjsinfo/main'
    headers['Cookie'] = "sjsinfo.session.id="+session.cookies.get('sjsinfo.session.id')
    response = session.post(url="http://oa.shijinshi.cn/sjsinfo/main/oa/workClockInRecord/clockInOrOut",headers=headers)
    if response.content.decode('utf-8') == 'in':
        logger.info(msg='You have been signed in!')
        print(time.ctime(time.time()),'oa sign in')
else:
    logger.info(msg='Failed to sign in')

