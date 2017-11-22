#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'DescribeLoadBalancerLog'  # 查询负载均衡实例列表


"""
loadBalancerId  必传 负载均衡的唯一ID
"""
region = 'sh'
params = {
    'loadBalancerId': 'lb-8cwh1nsb',
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
