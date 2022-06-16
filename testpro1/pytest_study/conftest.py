# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :conftest.py
# @author   : 声培 
# @Time     : 2022/6/14 0014 21:31
from typing import List

import items as items
import pytest

from requests_study.cookie_study import login


# @pytest.fixture(scope='function', autouse=True)
# def login_and_logout():
#     login()
#     print('在当前脚本文件中1，测试开始前只执行一次登录')
#     yield
#     print('在当前脚本文件中1，测试完成后只执行一次退出')

def pytest_collection_modifyitems(items: List["item"]):
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
