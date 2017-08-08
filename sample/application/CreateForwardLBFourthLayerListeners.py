#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'CreateForwardLBFourthLayerListeners'  # 创建应用型负载均衡四层监听器

"""
loadBalancerId 必传 负载均衡ID
listeners.n.loadBalancerPort 必传   负载均衡监听器监听端口
listeners.n.protocol         必传   负载均衡监听器监听协议 2：TCP， 3：UDP
listeners.n.listenerName     非必传 负载均衡监听器名字
listeners.n.sessionExpire	非必传	负载均衡监听器的会话保持时间，单位: 秒。内网负载均衡暂不支持会话保持,默认 0，表示不开启。
listeners.n.healthSwitch	非必传	负载均衡实例监听器是否开启健康检查：1（开启）、0（关闭）。默认值1，表示打开。
listeners.n.timeOut	非必传	负载均衡监听器健康检查的响应超时时间，可选值:2-60，默认值:2，单位:秒。响应超时时间要小于检查间隔时间。
listeners.n.intervalTime	非必传	负载均衡监听器检查间隔时间，默认值:5，可选值:5-300，单位:秒。
listeners.n.healthNum	非必传	负载均衡监听器健康阀值，默认值:3，表示当连续探测三次健康则表示该转发正常，可选值:2-10，单位：次。
listeners.n.unhealthNum	非必传	负载均衡监听器不健康阀值，默认值:3，表示当连续探测三次健康则表示该转发正常，可选值:2-10，单位：次。

"""
region = 'gz'
params = {
    'loadBalancerId': "lb-j2nvt9hq",
    'listeners.0.loadBalancerPort': 80,
    'listeners.0.protocol': 2,
    'listeners.0.listenerName': "test",
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
