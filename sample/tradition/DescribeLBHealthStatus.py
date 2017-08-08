#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

action = 'DescribeLBHealthStatus'  # 查询健康检查

"""
loadBalanceId 必传   负载均衡实例ID
listenerId   非必传  负载均衡监听器ID
"""
region = 'gz'
params = {
    'loadBalanceId': "lb-ddjl6hog",
    'listenerId': "lbl-gp2ztzlw",

}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
