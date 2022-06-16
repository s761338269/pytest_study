# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_fixture_study.py
# @author   : 声培 
# @Time     : 2022/6/14 0014 21:03
import time

import pytest

#定义fixture函数必须加上装饰器
# 前置处理一般可用做登录业务处理等，前置处理一般可用做登录业务处理等。
# session：表示在本次pytest执行中，该fixture函数不管被调用多少次，但只会被执行一次
# package：表示在本次pytest执行中，在当前包下该fixture函数不管被调用多少次，只会被执行一次
# module：表示在当前模块中，该fixture函数不管被调用多少次，只会被执行一次
# class：表示在当前类中，该fixture函数不管被调用多少次，只会被执行一次
# function：表示每个测试函数在调用fixture时，该fixture都会被执行,为空是默认是function
@pytest.fixture(scope='session')
def fixture_demo1():
    print('这是第一个fixture')
    yield time.time()
    print('用例执行完成后执行')
def test_a(fixture_demo1):
    print('第一个测试用例')
    print(fixture_demo1)

def test_b(fixture_demo1):
    print('这是第二个测试用例')
    print(fixture_demo1)

