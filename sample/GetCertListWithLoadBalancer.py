#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'GetCertListWithLoadBalancer'  # 获取证书关联的负载均衡

"""
certIds 必传 证书ID数组

"""
region = 'gz'
params = {
    'certIds.0': "05af1f32",
    # 'certIds.1':"0aac895c",
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
