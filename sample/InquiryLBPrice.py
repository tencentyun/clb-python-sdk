#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.QcloudApi.qcloudapi import QcloudApi

module = 'lb'
action = 'InquiryLBPrice'  # 查询负载均衡的价格
config = {
    'Region': 'gz',
    'secretId': 'AKIDAEJLDuynXJwOjtPhKm24AC4lXEyvm19C',
    'secretKey': '8A6xc8Tg6Ql4KROFG9sPlvuoY6pT2dGi',
    'method': 'get'
}

"""
loadBalancerType---yes   # 2： 公网属性  3：内网属性
timeUnit---yes   # h 按小时计费
"""

params = {
    'loadBalancerType': 2,
}

try:
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
