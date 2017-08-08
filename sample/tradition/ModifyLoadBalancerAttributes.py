#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

module = 'lb'
action = 'ModifyLoadBalancerAttributes'  # 修改传统型负载均衡的属性
config = {
    'Region': 'gz',
    'secretId': 'AKIDAEJLDuynXJwOjtPhKm24AC4lXEyvm19C',
    'secretKey': '8A6xc8Tg6Ql4KROFG9sPlvuoY6pT2dGi',
    'method': 'get'
}

"""
loadBalancerId 必传 负载均衡的唯一ID
loadBalancerName 非必传 负载均衡的新名字
domainPrefix   非必传  负载均衡的域名
"""
params = {
    'loadBalancerId': 'lb-5ahu7a8z',
    # 'loadBalancerName': 'xiaohao_loc',
    'domainPrefix': 'arlislb22',
}

try:
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
