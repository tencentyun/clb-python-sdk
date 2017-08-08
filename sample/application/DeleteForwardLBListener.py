#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'DeleteForwardLBListener'  # 删除转发型监听器

"""
loadBalancerId 必传 负载均衡ID
listenerId     必传 监听器ID

"""
region = 'gz'
params = {
    'loadBalancerId': "lb-7gmsxr7w",
    'listenerId': "lbl-pkqnqodm",
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
