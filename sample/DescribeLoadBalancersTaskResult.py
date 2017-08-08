#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'DescribeLoadBalancersTaskResult'  # 查询异步任务的执行状态

"""
requestId 必传 任务ID

"""
region = 'gz'
params = {
    "requestId": 12184482
}
try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
