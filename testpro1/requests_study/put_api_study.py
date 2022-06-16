# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :put_api_study.py
# @author   : 声培 
# @Time     : 2022/6/13 0013 13:47
import requests

def put(brand='Huawei', color='yellow', memorySize='64G',cpuCore='8核'):
    url = 'http://localhost:9090/com/phone'
    json = {
        "brand":"Huawei",
        "color":"yellow",
        "memorySize":"64G",
        "cpuCore":"8核",
        "price":"8848",
        "desc":"全新上市"
    }

    resp = requests.put(url=url, json=json)
    status_code = resp.status_code
    print(f'响应状态是{status_code}')
    json1 = resp.json()
    print(f'响应body体是{json1}')
    return resp

if __name__ == '__main__':
    put()

