# # coding:utf-8
# from selenium import webdriver
# from page.loginView import login
# from Common.startEnd import startEnd
# from Common.browser import browser
# import unittest
# class LoginTest(startEnd):
#     # def setUp(self):
#     #     self.driver=browser()
#
#
#     # zhangweihui zwh0814
#     def test_login_1(self):
#
#         l=login(self.driver)
#         usr="zhangweihui"
#         psd="zwh0814"
#         l.login_action(userName=usr, password=psd)
#         result=l.login_status()
#         self.assertTrue(result)
#         # driver.quit()
#
#     # zhangweihui zwh08141
#     # def test_login_2(self):
#     #     # self.driver = browser()
#     #     l=login(self.driver)
#     #     usr = "zhangweihui"
#     #     psd = "zwh08141"
#     #     l.login_action(userName=usr, password=psd)
#     #     result = l.login_status()
#     #     self.assertFalse(result)
#         # driver.quit()
#
#     #  # zhangweihui1 zwh0814
#     # def test_login_3(self):
#     #     # self.driver = browser()
#     #     l = login(self.driver)
#     #     usr = "zhangweihui1"
#     #     psd = "zwh0814"
#     #     l.login_action(userName=usr, password=psd)
#     #     result = l.login_status()
#     #     self.assertFalse(result)
#     #     # driver.quit()
#     # #
#     # #
#     # # def tearDown(self):
#     # #     self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main()