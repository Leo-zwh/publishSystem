# coding:utf-8

import unittest
from selenium import webdriver
import pytest
import time

class Testbb(unittest.TestCase):
    u'''测试用例a的集合'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.driver.get("https://www.cnblogs.com/yoyoketang/")


    def test_04(self):
        u'''用例1：用例1的操作步骤'''
        t = self.driver.title
        print(t)
        self.assertIn("悠悠", t)


    def test_05(self):
        u'''用例2：用例2的操作步骤'''
        t = self.driver.title
        print(t)
        self.assertIn("悠悠", t)

    def test_06(self):
        u'''用例3：用例3的操作步骤'''
        t = self.driver.title
        print(t)
        self.assertIn("悠悠", t)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    pytest.main(['-p','test_b.py'])