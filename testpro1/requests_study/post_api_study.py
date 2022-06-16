# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :post_api_study.py
# @author   : 声培 
# @Time     : 2022/6/13 0013 13:22
import requests

def post_login():
    url = 'http://localhost:9090/com/login'

    data = {
        'userName' : 'xiaochen',
        'password' : ''
    }
    resp = requests.post(url=url, data=data)
    status_code = resp.status_code
    print(f'响应状态码是{status_code}')
    result = resp.json()
    print(f'响应body是{result}')

def post_json():
    url = 'http://localhost:9090/com/register'

    json = {
        "userName": "shengpei",
        "password": "123456",
        "gender": 1,
        "phoneNum": "110",
        "email": "beihe@163.com",
         "address": "gz"
    }
    # headers ={
    #     'Content-Type':'application/json'
    # }
    resp = requests.post(url=url, json=json)
    status_code = resp.status_code
    print(f'响应状态码是{status_code}')
    result = resp.json()
    print(f'响应body是{result}')


if __name__ == '__main__':
    # post_login()
    post_json()