#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'DescribeForwardLBHealthStatus'

"""
loadBalancerIds  必传 负载均衡ID
"""
region = 'gz'
params = {
    'loadBalancerIds.0': "lb-7gmsxr7w",
    # 'loadBalancerIds.1':"lb-0c4ypb1m",
    # 'loadBalancerIds.1':"lb-mq65xc06",

}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
