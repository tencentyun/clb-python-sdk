#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'DeleteRewrite'  # 删除重定向

"""
loadBalancerId	是	String	负载均衡唯一ID
rewriteInfo	是	Array	重定向关系的转发规则，支持批量
sourceuListenerId	是	String	重定向监听器唯一Id
targetuListenerId	是	String	被重定向监听器唯一Id
"""
region = 'gz'
params = {
    'loadBalancerId': 'lb-6efswuxa',
    'sourceuListenerId': 'lbl-suource',
    'targetuListenerId': 'lbl-xxasaads',
    'delRewriteInfo.0.sourceLocation': 'loc-asdmamd',
    'delRewriteInfo.0.targetLocation': 'loc-eewqfqw'
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
