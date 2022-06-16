# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :get_api_study.py
# @author   : 声培 
# @Time     : 2022/6/13 0013 12:41
import requests

# 接口必需的信息
# 接口路径、请求headers、请求参数、响应状态码、响应body信息
def get():
    url = 'http://localhost:9090/com/getSku'  # 接口地址
    # 对于get接口来说，他的请求参数类型基本就是查询参数
    params = {
        'id': 1
    }
    # 接口请求信息已经准备好了，进行调用
    # resp是响应对象，包括了很多信息了，响应headers,响应状态码，响应body体信息
    resp = requests.get(url=url, params=params)
    status_code = resp.status_code
    print(f'状态码是：{status_code}')
    test = resp.text
    print(f'以字符串显示body体{test}')
    json1 = resp.json()
    print(f'响应信息是json格式的{json1}')
if __name__ == '__main__':
    get()