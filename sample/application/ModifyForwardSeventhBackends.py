#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'ModifyForwardSeventhBackends'  # 修改应用型七层监听器转发规则上云服务器的权重

"""
loadBalancerId 必传 负载均衡ID
listenerId     必传 负载均衡监听器ID
locationIds    非必传 负载均衡转发规则ID
domain         非必传 负载均衡转发域名
url            非必传 负载均衡转发路径
backends.n.instanceId 必传 机器的instanceId
backends.n.port       必传 机器的端口
backends.n.weight     非必传 机器的权重，默认10

"""
region = 'gz'
params = {
    'loadBalancerId': "lb-7gmsxr7w",
    'listenerId': "lbl-pkqnqodm",
    # 'listenerId':"lbl-f1oap4rk",
    # 'locationIds.0':"loc-3qwz5wvi",
    # 'locationIds.1':"loc-kac90jkw",
    'domain': "www.sayhaha.cn",
    'url': "/test1111",
    'backends.0.instanceId': "ins-kybxvfwm",
    'backends.0.port': 8035,
    'backends.0.weight': 29,
    'backends.1.instanceId': "ins-mt3sfc3q",
    'backends.1.port': 8020,
    'backends.1.weight': 29,
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
