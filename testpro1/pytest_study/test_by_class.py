# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_by_class.py
# @author   : 声培 
# @Time     : 2022/6/14 0014 10:36

#以类的形式编写测试用例

# 类必须要以Test开头
from requests_study.token_study import login


class Testlogin:
    # 用例1，用户密码正常登录
    def test_login(self):
        resp = login(userName='xiaochen',password='123456')
        status_code = resp.status_code
        assert status_code == 200
        code = resp.json()['code']
        # code为0证明登录业务成功。
        assert code == '0'
        message = resp.json()['message']
        assert message == 'success'

    # 测试用例2：账号为空，是否能成功登录
    def test_login_userisnull(self):
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


