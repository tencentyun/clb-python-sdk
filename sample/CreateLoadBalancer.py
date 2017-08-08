#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'CreateLoadBalancer'  # 创建负载均衡

"""
loadBalancerType 必传  2:公网属性  3:内网属性
forward  非必传        0：传统型 1:应用型，默认传统型
loadBalancerName 非必传  负载均衡名字，默认自动生成
domainPrefix     非必传  传统型公网负载均衡域名，默认自动生成
vpcId            非必传  网络属性
subnetId         非必传  子网属性
projectId        非必传  项目 ，默认为默认项目
number           非必传  购买负载均衡的个数，默认1
"""

region = 'gz'
params = {
    'loadBalancerType': 2,
    'forward': 1,
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
