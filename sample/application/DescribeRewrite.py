#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'DescribeRewrite'  # 查询重定向列表

"""
loadBalancerIds	非必传	负载均衡唯一ID
listenerIds	非必传	监听器唯一ID
locationIds	非必传	转发规则唯一ID
"""
region = 'gz'
params = {
    'loadBalancerIds.0': 'lb-6efswuxa',
    'listenerIds.0': 'lbl-20cxbf40',
    'locationIds.0': 'www.xxx.com'
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
