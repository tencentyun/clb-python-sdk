#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'CreateForwardLBSeventhLayerListeners'  # 创建应用型负载均衡七层监听器

"""
loadBalancerId 必传 负载均衡ID
listeners.n.loadBalancerPort 必传   负载均衡监听器监听端口
listeners.n.protocol         必传   负载均衡监听器监听协议 1：HTTP， 4：HTTPS
listeners.n.listenerName     非必传 负载均衡监听器名字
listeners.n.certContent      非必传 服务端证书的内容，当监听器协议为HTTPS时，如果没有设置certId，则此项必传
listeners.n.certKey          非必传 服务端证书的key，当监听器协议为HTTPS时，如果没有设置certId，则此项必传
listeners.n.certName         非必传 服务端证书的名称，当监听器协议为HTTPS时，如果没有设置certId，则此项必传
listeners.n.certId           非必传 服务端证书的ID，HTTPS监听器如果不填写此项则字段 certContent，certKey，certName 必传
listeners.n.certCaContent    非必传 客户端证书的内容，当监听器协议为HTTPS时，如果SSLMode=mutual，如果没有certCaId，则此项必传
listeners.n.SSLMode          非必传 HTTPS协议的认证类型，当监听器协议为HTTPS时，该字段必传，可选值 mutual：双向认证，unidirectional：单向认证
listeners.n.certCaName       非必传 客户端证书的名称，当监听器协议为HTTPS时，如果SSLMode=mutual，如果没有certCaId，则此项必传
listeners.n.certCaId         非必传 客户端证书的ID，如果SSLMode=mutual，同时没有上传客户端证书内容，则此项必传

"""
region = 'gz'
params = {
    'loadBalancerId': "lb-j2nvt9hq",
    'listeners.0.loadBalancerPort': 80,
    'listeners.0.protocol': 1,
    'listeners.0.listenerName': "test",
    # 'listeners.0.SSLMode':"mutual",
    # 'listeners.0.certId':"05af1f32",
    'listeners.0.SSLMode': "unidirectional",
    'listeners.0.certName': "server_ca2",
    'listeners.0.certContent': '''-----BEGIN CERTIFICATE-----
-----END CERTIFICATE-----
    ''',
    'listeners.0.certKey': """-----BEGIN RSA PRIVATE KEY-----
-----END RSA PRIVATE KEY-----
    """
    # 'listeners.0.certCaId':"989ed3d3",
    # 'listeners.0.certCaContent':'''-----BEGIN CERTIFICATE----- -----END CERTIFICATE-----''',
    # 'listeners.0.certCaName':"client_ca",
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
