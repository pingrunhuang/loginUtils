#!/bin/python
'''

'''

from selenium import webdriver
import time

homeurl = 'http://oa.shijinshi.cn/sjsinfo/main/login'
loginurl = 'http://oa.shijinshi.cn/sjsinfo/main?login'

username = "huangrunping"
password = "qwer1234"

def getGeckoDriver(executable_path='./driver/geckodriver.exe'):
    driver = webdriver.Firefox(executable_path=executable_path)
    return driver

def getPhantomJSDriver(path='./driver/phantomjs'):
    driver = webdriver.PhantomJS(path)
    return driver

def login(driver):
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys(username)
    password.send_keys(password)
    login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
    login_attempt.click()

if __name__ == '__main__':
    driver = getPhantomJSDriver()
    driver.get(homeurl)
    print(driver.source_page)