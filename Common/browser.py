# coding:utf-8
from selenium import webdriver
from Common.baseView import BaseView
import  time

def browser():
    driver = webdriver.Firefox()
    driver.get("http://yy.sdkservice.net/publishSystem/userLogin")
    time.sleep(2)
    return driver


if __name__ == '__main__':
    browser()

