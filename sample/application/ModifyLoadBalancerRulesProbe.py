#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'ModifyLoadBalancerRulesProbe'

"""
loadBalanceId 必传 负载均衡ID
listenerId  必传 监听器ID
locationId  必传 转发规则
newUrl      非必传 新的转发路径
sessionExpire 非必传 转发规则的会话保持时间
healthSwitch  非必传 转发规则的健康检查 ，默认打开
intervalTime  非必传 应用型负载均衡监听器转发规则的检查间隔，可选值:5-300
healthNum     非必传 应用型负载均衡监听器转发规则的健康阀值，可选值:2-10
unhealthNum   非必传 应用型负载均衡监听器转发规则的不健康阀值，可选值:2-10
httpHash      非必传 应用型负载均衡监听器转发规则的转发方式，可选值:wrr、ip_hash、least_conn
httpCode      非必传 应用型负载均衡监听器转发规则的健康状态码，可选值:1~31，默认31
httpCheckPath 非必传 应用型负载均衡监听器转发规则的探测路径，默认/，必须以/开头
httpCheckMethod 非必传 应用型负载均衡监听器转发规则的探测方法，可选值 HEAD， GET
httpCheckDomain 非必传 应用型负载均衡监听器转发规则的检查域名
"""
region='gz'
params = {
'loadBalancerId':"lb-g92k6j5s",
'listenerId':"lbl-4jiw2u16",   
'locationId':"loc-mm9a7z9q",   
'httpCheckDomain':'www.tencent.com',
'httpCheckMethod':'HEAD',
#'url':"~ php$",
# 'httpCode':31,
# 'httpCheckPath':"/image/qq/com/", 
# 'sessionExpire':221,  
# 'healthSwitch':1, 
# 'intervalTime':300,   
# 'healthNum':2,
# 'unhealthNum':3,  
# #'httpHash':"wrr",
# 'httpHash':"ip_hash", 
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
