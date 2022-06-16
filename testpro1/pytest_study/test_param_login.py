# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_param_login.py
# @author   : 声培 
# @Time     : 2022/6/14 0014 16:56

import pytest
from requests_study.cookie_study import login

#第一步，将测试用例数据转化成Python中列表套列表
test_data = [
    ['xiaochen', '123456', 200, '0', 'success'],
    ['',         '123456', 200, '1', '参数为空'],
    ['xiaochen', '',       200, '1', '参数为空']
]
# 第二步，用pytest的装饰器，读取上述数据，将其数据传达用例函数。
@pytest.mark.parametrize('userName, password, expect_status_code, expect_code, expect_message', test_data)
def test_login(userName, password, expect_status_code, expect_code, expect_message):
    resp = login(userName=userName,password=password)
    status_code = resp.status_code
    assert status_code == expect_status_code
    code = resp.json()['code']
    # assert code == expect_code
    pytest.assume(code==expect_code, f'实际值{code},期望值：{expect_code}')
    message = resp.json()['message']
    # assert message == expect_message
    pytest.assume(message == expect_message, f'实际值{message},期望值：{expect_message}')
