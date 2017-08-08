#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'DeleteLoadBalancers'  # 删除负载均衡

"""
loadBalancerIds.n  必传 负载均衡ID

"""
region = 'gz'
params = {
    'loadBalancerIds.0': "lb-815g2nuv",
    # 'loadBalancerIds.1':"lb-qzaci6au",
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
