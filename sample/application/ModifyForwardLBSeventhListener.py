#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'ModifyForwardLBSeventhListener'  # 修改应用型负载均衡七层监听器属性

"""
loadBalancerId	是	String	负载均衡实例统一ID，即 unLoadBalancerId，可通过DescribeLoadBalancers接口同时入参forward字段为1或者-1来查询。
listenerId	是	String	应用型负载均衡监听器ID，可通过 DescribeForwardLBListeners 接口查询。
listenerName	否	String	应用型负载均衡监听器名称。
SSLMode	否	String	HTTPS协议监听器的认证类型, unidirectional:单向认证，mutual:双向认证。
certId	否	String	HTTPS协议监听器新的服务端证书ID。
certCaId	否	String	HTTPS协议监听器新的客户端证书ID。
certCaContent	否	String	HTTPS协议监听器新的客户端证书内容。
certCaName	否	String	HTTPS协议监听器新的客户端证书名称。
certContent	否	String	HTTPS协议监听器新的服务端证书内容。
certKey	否	String	HTTPS协议监听器新的服务端证书的密钥。
certName	否	String	HTTPS协议监听器新的服务端证书的名称。
"""

region = 'gz'
params = {
    'loadBalancerId': "lb-7gmsxr7w",
    'listenerId': "lbl-jb2kkehy",
    # 'listenerId':"lbl-pkqnqodm",
    'listenerName': "newName",
    # 'SSLMode':"mutual",
    'SSLMode': "unidirectional",
    'certId': "05af1f32",
    # 'certContent':'''-----BEGIN CERTIFICATE----------END CERTIFICATE-----''',
    # 'certKey':'''-----BEGIN RSA PRIVATE KEY----------END RSA PRIVATE KEY-----''',
    # 'certName':"11111111",
    # 'certCaId':"05da2232",
    # 'certCaContent':'''-----BEGIN CERTIFICATE----- -----END CERTIFICATE-----''',
    # 'certCaName':"haha11",
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
