#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'ModifyForwardLBFourthListener'  # 修改应用型负载均衡七层监听器属性

"""
loadBalancerId	必传 	负载均衡实例ID
listenerId      必传	 负载均衡监听器ID
listenerName	非必传	监听器名称。
sessionExpire	非必传	会话保持时间，0 表示关闭，可选30-3600
healthSwitch	非必传	是否开启健康检查：1（开启）、0（关闭）
timeOut         非必传	响应超时时间，可传值为 2-60 秒
intervalTime	非必传	检查间隔，可选值：5-300
healthNum	非必传	健康阀值，可选值:2-10
unhealthNum	非必传 不健康阀值，可选值：2-10
"""

region = 'gz'
params = {
    'loadBalancerId': "lb-7gmsxr7w",
    'listenerId': "lbl-jb2kkehy",
    'listenerName': "newName",

}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
