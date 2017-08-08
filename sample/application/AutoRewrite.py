#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'AutoRewrite'  # 自动重定向配置

"""
loadBalancerId	必传	负载均衡唯一ID
listenerId	必传	监听器唯一ID
domains	必传 	需要重定向的domain，支持批量

"""
region = 'gz'
params = {
    'loadBalancerId': 'lb-6efswuxa',
    'listenerId': 'lbl-20cxbf40',
    'domains.0': 'www.xxx.com'
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
