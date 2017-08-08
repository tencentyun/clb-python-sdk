#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

action = 'ModifyLoadBalancerBackends'  # 修改负载均衡后端机器的权重

"""
loadBalancerId  必传  负载均衡实例ID
backends.n.instanceId 必传  云服务器的唯一ID
backends.n.weight 必传  绑定的云服务器的权重, 取值范围 0-100，默认 10。
"""
region = 'gz'
params = {
    'loadBalancerId': "",
    'backends.1.instanceId': "ins-6ef0vd2i",
    'backends.1.weight': 99,
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
