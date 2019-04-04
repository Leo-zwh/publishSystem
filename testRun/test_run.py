# coding=utf-8
import unittest
import os
from tomorrow import threads
import HTMLTestRunner


# 获取路径
curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
case_path = os.path.join(curpath, "testCase")
if not os.path.exists(case_path):
    print("测试用例需放到‘testCase’文件目录下")
    os.mkdir(case_path)
report_path = os.path.join(curpath, "report1")
if not os.path.exists(report_path): os.mkdir(report_path)


def add_case(case_path=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    print(discover)
    return discover


# def run(test_suit):
#     result = BeautifulReport(test_suit)
#     result.report(filename='report.html', description='测试deafult报告', report_dir=reportpath)

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())

    # html报告文件路径
    report_abspath = os.path.join(report_path, "result.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(add_case())
    fp.close()