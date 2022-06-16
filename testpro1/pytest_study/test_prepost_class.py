# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_prepost_class.py
# @author   : 声培 
# @Time     : 2022/6/14 0014 14:58
import pytest
from requests_study.cookie_study import login, query

@pytest.fixture(scope='class',autouse=True)
def login_and_logout():
    login()
    print('在当前类中，测试开始前只执行一次登录')
    yield
    print('在当前类中，测试完成后只执行一次退出')

class TestQuery:

    # # 前置动作完成登录
    # def setup_class(self):
    #     login()
    #     # 因为login默认已经有默认参数，这里可以为空
    #     print('在当前类中，测试开始前只执行一次登录')
    #
    # #后置动作退出
    # def teardown_class(self):
    #     print('在当前类中，测试完成后只执行一次退出')


    #测试用例1：余额正确查询
    def test_query(self):
        # 调用查询余额接口，传入要查询的用户名
        # 因为上面传入的是xiaochen，所以这里也要传入xiaochen
        resp = query(userName='xiaochen')
        #断言，判断响应码是否是200
        status_code = resp.status_code
        assert status_code == 200
        message = resp.json()['message']
        assert message == 'success'
        # 判断响应信息中的code字段是否是0
        code = resp.json()['code']
        assert code == '0'

    # 测试用例2：用户未登录能否查询
    def test_query1(self):
        resp = query(userName='liming')
        status_code = resp.status_code
        assert status_code == 200
        message = resp.json()['message']
        assert message == '用户未登录'
        code = resp.json()['code']
        assert code == '1'

class TestQuery2:

    # # 前置动作完成登录
    # def setup_class(self):
    #     login()
    #     # 因为login默认已经有默认参数，这里可以为空
    #     print('在当前类中，测试开始前只执行一次登录')
    #
    # #后置动作退出
    # def teardown_class(self):
    #     print('在当前类中，测试完成后只执行一次退出')


    #测试用例1：余额正确查询
    def test_query(self):
        # 调用查询余额接口，传入要查询的用户名
        # 因为上面传入的是xiaochen，所以这里也要传入xiaochen
        resp = query(userName='xiaochen')
        #断言，判断响应码是否是200
        status_code = resp.status_code
        assert status_code == 200
        message = resp.json()['message']
        assert message == 'success'
        # 判断响应信息中的code字段是否是0
        code = resp.json()['code']
        assert code == '0'

    # 测试用例2：用户未登录能否查询
    def test_query1(self):
        resp = query(userName='liming')
        status_code = resp.status_code
        assert status_code == 200
        message = resp.json()['message']
        assert message == '用户未登录'
        code = resp.json()['code']
        assert code == '1'