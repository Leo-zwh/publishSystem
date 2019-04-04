# coding:utf-8
from selenium import webdriver
from Common.browser import browser
import unittest

class startEnd(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()


