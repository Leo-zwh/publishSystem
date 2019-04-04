# coding:utf-8
import unittest
from BeautifulReport import BeautifulReport
import os
from tomorrow import threads

# 加载地址
curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(curpath)
casepath= os.path.join(curpath,'testCase')
print(casepath)
reportpath=os.path.join(curpath,'Report')
print(reportpath)
if not os.path.exists(casepath):
    print("测试用例需放到‘case’文件目录下")
    os.mkdir(casepath)
if not os.path.exists(reportpath): os.mkdir(reportpath)


# 加载用例
def add_case():
    discover=unittest.defaultTestLoader.discover(casepath, pattern='test*.py',top_level_dir=None)
    return discover

@threads(2)
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html', description='测试deafult报告', report_dir=reportpath)

if __name__ == "__main__":
    # 用例集合
    cases = add_case()

    print(cases)
    for i in cases:
        print(i)
        run(i)