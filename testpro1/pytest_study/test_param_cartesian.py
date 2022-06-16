# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_param_cartesian.py
# @author   : 声培 
# @Time     : 2022/6/14 0014 17:16
import pytest

from requests_study.put_api_study import put

brand_data = ['HUawei','xiaomi','oppo']
color_data = ['yellow','red','white']
memorySize_data = ['64G','128G','256G']
cpuCore_data = ['4核','8核','12核','16核']
expect_status_code_data = [200]
expect_code_data = ['0']
expect_message_data = ['更新成功']
# 采用笛卡尔积后，形成的测试数据条数总计是3*3*3*4*1*1*1=108条
@pytest.mark.parametrize('brand',brand_data)
@pytest.mark.parametrize('color',color_data)
@pytest.mark.parametrize('memorySize',memorySize_data)
@pytest.mark.parametrize('cpuCore',cpuCore_data)
@pytest.mark.parametrize('expect_status_code',expect_status_code_data)
@pytest.mark.parametrize('expect_code_data',expect_code_data)
@pytest.mark.parametrize('expect_message',expect_message_data)
def test_put(brand, color, memorySize, cpuCore, expect_status_code, expect_code_data, expect_message):
    # 调用接口，传递测试数据，拿到响应对象
    resp = put(brand=brand,color=color,memorySize=memorySize,cpuCore=cpuCore)
    status_code = resp.status_code
    assert status_code == expect_status_code
    code = resp.json()['code']
    assert code == expect_code_data
    message = resp.json()['message']
    assert message == expect_message
