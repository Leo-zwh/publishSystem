# coding:utf-8
from selenium import webdriver
from Common.common import browser
from Common.common import Common
from selenium.common.exceptions import NoSuchElementException
from Common.browser import browser
import time

class login(Common):
    # driver = webdriver.Firefox()
    # driver.get("http://yy.sdkservice.net/publishSystem/userLogin")
    # driver.implicitly_wait(10)
    # driver = browser()

    def login_action(self,userName,password):
        self.driver.find_element_by_xpath(".//*[@id='loginFrm']/input[1]").send_keys(userName)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='loginFrm']/input[2]").send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='loginFrm']/div[2]").click()
        time.sleep(2)




    def login_status(self):
        try:
            t=self.driver.find_element_by_xpath("html/body/div[2]/div[1]/div/div[2]").text
            print(t)
            return True
        except NoSuchElementException:
            return False
        else:
            return False








if __name__ == '__main__':
    driver=browser()
    # l=login(driver)
    # userName="zhangweihui"
    # password="zwh0814"
    # l.login_action(userName,password)