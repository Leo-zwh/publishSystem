# coding:utf-8
import unittest
import os

# 获取路径
curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
case_path = os.path.join(curpath, "testCase")
if not os.path.exists(case_path):
    print("测试用例需放到‘testCase’文件目录下")
    os.mkdir(case_path)
report_path = os.path.join(curpath, "report")
print(report_path)
if not os.path.exists(report_path): os.mkdir(report_path)
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_case())