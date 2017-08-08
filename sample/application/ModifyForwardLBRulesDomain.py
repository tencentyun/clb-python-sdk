#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'ModifyForwardLBRulesDomain'


"""
loadBalancerId	必传 	负载均衡实例ID
listenerId	必传 	应用型负载均衡监听器ID
domain	必传 监听器下旧域名。
newDomain	必传 长度限制为1-80。有三种使用格式:非正则表达式格式，通配符格式，正则表达式格式。非正则表达式格式只能使用字母、数字、‘-’、‘.’。通配符格式的使用 ‘*’ 只能在开头或者结尾。正则表达式以'~'开头。
"""
region='gz'
params = {
    'loadBalancerId':"lb-ku3ipkme",
    'listenerId':"lbl-2f42mdno",
    'domain':"www.domin.edu",
    'newDomain':"www.tencent.com"
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
