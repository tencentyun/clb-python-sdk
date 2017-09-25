#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'DescribeLoadBalancerBackends'  # 查询负载均衡后端绑定的机器

"""
loadBalancerId	必传 负载均衡ID
"""
region = 'gz'
params = {
    'loadBalancerId': "lb-rbxrst45",
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)

except Exception, e:
    print 'exception:', e
