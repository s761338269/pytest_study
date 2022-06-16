# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :cookie_study.py
# @author   : 声培 
# @Time     : 2022/6/13 0013 16:48
import requests

#多个接口使用同一个session对象的话，他会自动的帮我们去管理和关联cookie
session = requests.session()

def login(userName='xiaochen',password='123456'):
    url = 'http://localhost:9090/bank/api/login'

    data = {
        'userName': userName,
        'password': password
    }
    resp = session.post(url=url, data=data)
    status_code = resp.status_code
    print(f'响应状态码是{status_code}')
    result = resp.json()
    print(f'响应body是{result}')
    return resp
def query(userName='xiaochen'):
    url = 'http://localhost:9090/bank/api/query'
    # 查询参数
    params = {
        'userName':userName
    }
    resp = session.get(url=url, params=params)
    status_code = resp.status_code
    print(f'响应状态码是{status_code}')
    result = resp.json()
    print(f'响应body是{result}')
    return resp

if __name__ == '__main__':
    login()
    query()