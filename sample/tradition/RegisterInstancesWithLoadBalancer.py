#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

action = 'RegisterInstancesWithLoadBalancer'  # 绑定机器到负载均衡

"""
loadBalancerId	必传 负载均衡实例ID，可使用loadBalancerId 或 unLoadBalancerId，推荐使用unLoadBalancerId，可通过DescribeLoadBalancers接口查询。
backends.n.instanceId	必传	云服务器的唯一ID，可通过DescribeInstances接口返回字段中的 unInstanceId 字段获取
backends.n.weight	非必传	云服务器的权重，取值范围 0-100，默认为 10。
"""
region = 'gz'
params = {
    'loadBalancerId': "lb-ayvbjw1u",
    'backends.0.instanceId': "ins-jiis9uki",
    'backends.0.weight': 30,
    # 'backends.1.instanceId':"ins-652rev1e",
    # 'backends.1.weight':30
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
