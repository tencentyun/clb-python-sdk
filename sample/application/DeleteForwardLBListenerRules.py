#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'DeleteForwardLBListenerRules'  # 删除应用型负载均衡的转发规则

"""
loadBalancerId 必传 负载均衡ID
listenerId     必传 监听器ID
locationIds.n  非必传 转发规则ID，默认全部删除
domain         非必传 转发规则域名，默认不做过滤条件
url            非必传 转发规则路径，默认不做过滤条件
"""
region = 'gz'

params = {
    'loadBalancerId': 'lb-6efswuxa',
    'listenerId': 'lbl-fh7o7b9o',
    'locationIds.0': "loc-jw3a7y2o",
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
