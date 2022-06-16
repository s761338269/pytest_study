# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :file_study.py
# @author   : 声培 
# @Time     : 2022/6/13 0013 22:18
import requests
session = requests.session()

def upload_file():
    url = 'http://localhost:9090/file/api/upload2'

    files = {
        'file': open(r'C:\Users\Administrator\Desktop\龙之矛.txt', mode='rb')
    }
    resp = session.post(url=url, files=files)
    status_code = resp.status_code
    print(f'状态码是：{status_code}')
    test = resp.text
    print(f'响应内容body体{test}')

if __name__ == '__main__':
    upload_file()
