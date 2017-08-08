#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

action = 'DescribeLoadBalancerListeners'  # 查询负载均衡的监听器

"""
loadBalancerId	必传 负载均衡实例 ID
listenerIds.n	非必传 负载均衡监听器ID。
protocol	    非必传 监听器协议类型 1：HTTP，2：TCP，3：UDP，4：HTTPS。
loadBalancerPort 非必传	负载均衡监听器端口。
status	非必传	负载均衡监听器的状态，当输入负载均衡监听器ID来查询时，忽略该字段。
"""
region = 'gz'
params = {
    'loadBalancerId': "lb-ddjl6hog",
    'listenerIds.0': "lbl-gp2ztzlw",
    # 'listenerIds.1':"lbl-ne2v3kqw",
    # 'protocol':4,
    # 'loadBalancerPort':2558,
}

try:
    service = QcloudApi(region='gz')
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
