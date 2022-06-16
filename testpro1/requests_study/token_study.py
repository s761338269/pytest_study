# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :token_study.py
# @author   : 声培 
# @Time     : 2022/6/13 0013 17:26
import requests

session = requests.session()

def login(userName='xhaiochen',password='123456'):
    url = 'http://localhost:9090/bank/api/login2'

    data ={
        'userName':userName,
        'password':password
    }

    # 发起请求
    resp = session.post(url=url, data=data)
    #查看响应
    status_code = resp.status_code
    print(f'响应状态码是：{status_code}')
    json1 = resp.json()
    print(f'响应body体是：{json1}')
    print(type(resp.json()))
    # 全局变量，方便下面的函数使用
    global token
    # 需要用到token才能完成下一步的接口测试
    token = resp.json()['data']
    return resp

def query():
    url = 'http://localhost:9090/bank/api/query2'

    params ={
        'userName':'xiaochen'
    }
    headers ={
        'testfan-token':token
    }
    resp = session.get(url=url, params=params, headers=headers)
    # 查看响应
    status_code = resp.status_code
    print(f'响应状态码是：{status_code}')
    json1 = resp.json()
    print(f'响应body体是：{json1}')

if __name__ == '__main__':
    login()
    query()
