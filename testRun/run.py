# coding:utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import os

# 获取路径
curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(curpath)

# 用例路径
casepath = os.path.join(curpath, 'testCase')
print(casepath)

# 报告路径
reportpath = os.path.join(curpath, 'report')
print(reportpath)

# 添加用例
def add_case():
    discover=unittest.defaultTestLoader.discover(start_dir=casepath, pattern="test*.py", top_level_dir=None)
    return discover

# 执行用例


def run_case(all_case, report_path=reportpath, nth=0):
    report_abspath = os.path.join(reportpath,'result%s.html'%nth)
    fp = open(report_abspath, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试发布系统-测试报告', description='具体情况')

    runner.run(all_case)
    fp.close()

if __name__ == '__main__':
    # 用例集合
    cases = add_case()

    # 之前是批量执行，这里改成for循环执行
    for i, j in zip(cases, range(len(list(cases)))):
        run_case(i, nth=j)  # 执行用例，生成报告

