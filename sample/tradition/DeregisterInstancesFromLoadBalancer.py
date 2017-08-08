#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

action = 'DeregisterInstancesFromLoadBalancer'  # 从负载均衡上解绑机器

"""
loadBalancerId 必传 负载均衡实例ID
backends.n.instanceId 必传 云服务器的唯一ID
"""
region = 'gz'
params = {
    'loadBalancerId': "lb-eqluo3c6",
    'backends.0.instanceId': "ins-rro4g1xm"
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
