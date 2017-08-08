#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'CreateForwardLBListenerRules'  # 创建应用型负载均衡的转发规则

"""
loadBalancerId  必传 负载均衡ID
listenerId      必传 监听器ID
rules.n.domain  必传 转发规则的转发域名
rules.n.url     必传 转发规则的转发路径
rules.n.sessionExpire 非必传 规则是否开启会话保持，可选值 0 或者30-3600，默认0，不开启
rules.n.healthSwitch  非必传 规则是否开启健康检查，默认1，开启
rules.n.intervalTime  非必传 规则的健康探测间隔，可选值 5-300，默认5
rules.n.healthNum     非必传 规则的建康阀值，可选值2-10，默认3
rules.n.unhealthNum   非必传 规则的不建康阀值，可选值2-10，默认3
rules.n.httpHash      非必传 规则的转发方式，可选值wrr 权重轮询， ip_hash 基于cookie的会话保持， least_conn 最小连接数，默认wrr
rules.n.httpCode      非必传 健康检查的状态码，可选值 1-31，默认31
rules.n.httpCheckPath 非必传 健康检查路径，默认/
rules.n.httpCheckDomain 非必传 健康检查域名，若转发域名非正则切非通配符，该字段与转发域名一致，否则必传
"""
region = 'gz'
params = {
    'loadBalancerId': 'lb-g92k6j5s',
    'listenerId': 'lbl-dexltb70',
    'rules.0.domain': 'www.tencent.com',
    'rules.0.url': '/',
    'rules.0.healthSwitch': 1,
    'rules.0.intervalTime': 10,
    'rules.0.healthNum': 3,
    'rules.0.unhealthNum': 3,
    'rules.0.httpHash': 'least_conn',
    'rules.0.httpCode': 16,
    'rules.0.httpCheckPath': '/test1',
    'rules.0.httpCheckDomain': 'www.lbapi.com',
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
