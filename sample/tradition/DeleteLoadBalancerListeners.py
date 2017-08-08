#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

action = 'DeleteLoadBalancerListeners'

"""
loadBalancerId--yes
listenerIds.n---yes
"""

region = 'gz'
params = {
    'loadBalancerId': "lb-ayvbjw1u",
    'listenerIds.0': "lbl-a7rp6p7s",
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
