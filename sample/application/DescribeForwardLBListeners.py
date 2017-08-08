#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'DescribeForwardLBListeners'  # 查询应用型负载均衡的监听器

"""
loadBalancerId  必传 负载均衡ID
listenerIds.n   非必传 负载均衡监听器ID，默认查询全部监听器
protocol        非必传 负载均衡监听器协议，默认全部
loadBalancerPort 非必传 负载均衡监听器监听端口，默认全部

"""
region = 'gz'
params = {
    'loadBalancerId': "lb-8vy9fs3l",
    # 'listenerIds.0':"lbl-fgrpix2m",
    # 'listenerIds.1':"lbl-ne2v3kqw",
    # 'protocol':4,
    # 'loadBalancerPort':8090,
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
