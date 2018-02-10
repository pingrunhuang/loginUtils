'''
This script is to read the captcha from a webpage 
'''

# for opening up the image
import subprocess
import requests


def getCaptcha(CaptchaImagePath, HEADERS):
    captchaImgUrl = 'https://passport.lagou.com/vcode/create?from=register&refresh=%s' % time.time()
    # write the captcha image to the path
    with open(CaptchaImagePath, 'wb') as f:
        f.write(session.get(captchaImgUrl, headers=HEADERS).content)

    # open the captcha image
    if sys.platform.find('darwin') >= 0:
        subprocess.call(['open', CaptchaImagePath])
    elif sys.platform.find('linux') >= 0:
        subprocess.call(['xdg-open', CaptchaImagePath])
    else:
        os.startfile(CaptchaImagePath)

    # return the code 
    captcha = input("请输入当前地址(% s)的验证码: " % CaptchaImagePath)
    print('你输入的验证码是:% s' % captcha)
    return captcha