#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'DescribeLoadBalancers'  # 查询负载均衡实例列表


"""
loadBalancerIds.n  非必传 负载均衡的唯一ID
forward            非必传 1：应用型负载均衡 0：传统型负载均衡 -1：传统型与应用型负载均衡 ，默认0
loadBalancerType   非必传 负载均衡的类型
loadBalancerName   非必传 负载均衡的名字
domain             非必传 负载均衡的域名
loadBalancerVips.n 非必传 负载均衡的 VIP
offset             非必传 数据偏移量，默认为0
limit              非必传 返回负载均衡的个数，默认为20
orderBy            非必传 loadBalancerName：按照名字排序, createTime: 按照购买时间排序，domain: 按照域名排序，loadBalancerType：按照类型排序，默认按照购买时间排序
orderType          非必传 排序方式 1：倒序 0：顺序，默认倒序
searchKey          非必传 模糊搜索，匹配负载均衡的VIP 、名字、域名
projectId          非必传 负载均衡的项目ID
backendLanIps.n    非必传 负载均衡后端绑定的机器的外网IP
backendWanIps.n    非必传 负载均衡后端绑定的机器的外网IP
withRs             非必传 1：查询绑定了机器的负载均衡 0： 查询没有绑定机器的负载均衡 2：是否绑定机器不作为过滤条件。默认 2
"""
region = 'gz'
params = {
    'forward': -1,
    'loadBalancerType': 2,
    # 'loadBalancerName':'lb',
    # 'loadBalancerVips.0':'183.60.249.82',
    # 'loadBalancerVips.1':'183.60.249.57',
    # 'backendWanIps.0':'183.60.249.41',
    # 'offset':0,
    # 'limit':100,
    # 'orderBy':'loadBalancerName',
    # 'orderType':0,
    # 'searchKey':'183.60.249.41',
    # 'projectId':0,
    # 'backendLanIps.0':'10.104.63.47',
    # 'withRs':2
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
