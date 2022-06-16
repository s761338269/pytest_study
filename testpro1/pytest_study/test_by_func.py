# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_by_func.py
# @author   : 声培 
# @Time     : 2022/6/13 0013 23:25

# 以函数形式编写测试用例

from requests_study.cookie_study import login

# 测试用例1：账号密码正常，是否能成功登录
def test_login():
    # 调用目标接口，传入测试数据，resp是响应对象
    resp = login(userName='xiaochen', password='123456')
    # 针对接口响应结果判断
    #针对结果做判断的这个过程，我们把他叫做断言
    #对于接口来说，我们关注的是响应状态码，以及响应body信息的核心字段
    status_code = resp.status_code
    assert status_code == 200 #assert是断言
    # 针对响应body体信息中的code字段做判断，code为0即登录业务成功。
    resp_json = resp.json()
    print(resp_json)
    code = resp.json()['code']
    assert code == '0'
    message = resp.json()['message']
    assert message == 'success'

# 测试用例2：账号为空，是否能成功登录
def test_login_userisnull():
    # 调用目标接口，传入测试数据，resp是响应对象
    resp = login(userName='', password='123456')
    status_code = resp.status_code
    assert status_code == 200  # assert是断言
    # 针对响应body体信息中的code字段做判断，code为1即登录业务失败。
    resp_json = resp.json()
    print(resp_json)
    code = resp.json()['code']
    assert code == '1'
    message = resp.json()['message']
    assert message == '参数为空'