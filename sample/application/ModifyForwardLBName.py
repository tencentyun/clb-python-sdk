#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi


action = 'ModifyForwardLBName'  # 修改应用型负载均衡名字


"""
loadBalancerId  必传  负载均衡ID
loadBalancerName 必传 负载均衡的新名字
"""
region = 'gz'

params = {
    'loadBalancerId': 'lb-8vy9fs3l',
    'loadBalancerName': '11111166111111111t',
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)

except Exception, e:
    print 'exception:', e
