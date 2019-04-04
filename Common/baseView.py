# coding:utf-8
class BaseView():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loctor):
        return self.driver.fing_element(loctor)