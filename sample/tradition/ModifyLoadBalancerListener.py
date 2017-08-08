#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

module = 'lb'
action = 'ModifyLoadBalancerListener'  # 更改负载均衡后端监听器

"""
loadBalancerId	必传 	负载均衡实例ID
listenerId	必传 	负载均衡监听器ID
listenerName	非必传	监听器名称。
sessionExpire	非必传	会话保持时间，0 表示关闭，可选值30-3600
healthSwitch	非必传	是否开启健康检查：1（开启）、0（关闭）。
timeOut	非必传	响应超时时间，可传值为 2-60 秒；公网的HTTP、HTTPS协议监听器的响应超时时间暂时不能设置，默认值5秒。
intervalTime	非必传	检查间隔，可选值：5-300。默认值:5。
healthNum	非必传	健康阀值，可选值:2-10。
unhealthNum	非必传	不健康阀值,可选值：2-10。
httpHash	非必传	负载均衡监听器转发的方式。仅公网有日租（监听器为HTTP、HTTPS）类型才支持此字段，可传值：wrr、ip_hash，least_conn
httpCode	非必传	对于HTTP、HTTPS协议的监听器，以该返回码来判断健康与否。可选值:1~31
httpCheckPath	非必传	对于HTTP、HTTPS协议的监听器，健康检查的路径，默认/，必须以/开头。
SSLMode	非必传	HTTPS协议监听器的认证类型,unidirectional:单向认证，mutual：双向认证。
certId	非必传	HTTPS协议监听器新的服务端证书ID。
certCaId	非必传	HTTPS协议监听器新的客户端证书ID。
certCaContent	非必传	HTTPS协议监听器新的客户端证书内容。
certCaName	非必传	HTTPS协议监听器新的客户端证书名称。
certContent	非必传	HTTPS协议监听器新的服务端证书内容。
certKey	非必传	HTTPS协议监听器新的服务端证书的密钥。
certName	非必传	HTTPS协议监听器新的服务端证书的名称。
"""
region = 'gz'
params = {
    'loadBalancerId': "lb-eubisqp8",
    'listenerId': "lbl-riqk4i14",
    'httpHash': "ip_hash",
    # 'httpCode':31,
    # 'httpCheckPath':"/image/qq/com/",
    # 'listenerName':"arlistest",
    'sessionExpire': 0,
    # 'healthSwitch':1,
    # 'timeOut':5,
    # 'intervalTime':300,
    # 'healthNum':2,
    # 'unhealthNum':2,
    # 'httpHash':"wrr",
    # 'SSLMode':"mutual",
    # 'SSLMode':"unidirectional",
    # 'certId':"9945e3e3",
    # 'certContent':'''-----BEGIN CERTIFICATE----------END CERTIFICATE-----''',
    # 'certKey':'''-----BEGIN RSA PRIVATE KEY----------END RSA PRIVATE KEY-----''',
    # 'certName':"11111111",
    # 'certCaId':"989ed3d3",
    # 'certCaContent':'''-----BEGIN CERTIFICATE----------END CERTIFICATE-----''',
    # 'certCaName':"haha1",
}

try:
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
