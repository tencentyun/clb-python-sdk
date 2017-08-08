#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

sys.path.append('..')

from src.QcloudApi.qcloudapi import QcloudApi

action = 'CreateLoadBalancerListeners'  # 创建负载均衡监听器

"""
loadBalancerId  必传 负载均衡实例ID
listeners.n.loadBalancerPort	必传 负载均衡监听器的监听接口，可选值1~65535。listeners为数组，可以创建多个监听器，n为下标。
listeners.n.instancePort	必传 负载均衡实例监听器后端云服务器监听端口，可选值：1~65535。
listeners.n.protocol	必传 	负载均衡实例监听器协议类型 1：HTTP，2：TCP，3：UDP，4：HTTPS。公网类型负载均衡实例支持 HTTP、UDP、TCP、HTTPS 协议；
                                内网类型负载均衡实例支持 TCP 和 UDP 协议。
listeners.n.listenerName  非必传 负载均衡监听器的监听名称。
listeners.n.sessionExpire 非必传 负载均衡监听器的会话保持时间，单位：秒。可选值：30~3600 默认关闭
listeners.n.healthSwitch  非必传 负载均衡实例监听器是否开启健康检查：1（开启）、0（关闭）。默认值1，表示打开。
listeners.n.timeOut	否	  非必传	负载均衡监听器健康检查的响应超时时间，可选值：2-60，默认值：2，单位:秒。响应超时时间要小于检查间隔时间。
                                公网 HTTP、HTTPS 协议的监听器响应超时时间暂不能设置。
listeners.n.intervalTime  非必传	负载均衡监听器检查间隔时间，默认值：5，可选值：5-300，单位：秒。

listeners.n.healthNum	否	Int	负载均衡监听器健康阀值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2-10，单位：次。
listeners.n.unhealthNum	否	Int	负载均衡监听器不健康阀值，默认值：3，表示当连续探测三次不健康则表示该转发不正常，可选值：2-10，单位：次。
listeners.n.httpHash	否	Int	负载均衡监听器转发的方式。仅公网有日租（监听器为HTTP、HTTPS）类型才支持此字段，可传值：wrr、ip_hash、least_conn 默认为wrr。
listeners.n.httpCode	否	Int	对于 HTTP、HTTPS 协议的监听器，以该返回码来判断健康与否。可选值：1~31，默认31。
1 代表返回值 1xx 表示健康，2 代表返回 2xx 表示健康，4 代表返回 3xx 表示健康，8 代表返回 4xx 表示健康，16 代表返回 5xx 表示健康。
若返回多种表示健康，则将相应的值累加。
listeners.n.httpCheckPath	否	String	对于HTTP、HTTPS协议的监听器健康检查的路径。默认 /，必须以 / 开头。
listeners.n.SSLMode	否	String	HTTPS 协议的认证类型。unidirectional:单向认证；mutual：双向认证。HTTPS协议监听器必选此项。
listeners.n.certId	否	String	服务端证书的ID，HTTPS监听器如果不填写此项则必须上传证书，包括certContent，certKey，certName
listeners.n.certCaId	否	String	客户端证书的ID，如果SSLMode=mutual，HTTPS监听器如果不填写此项则必须上传客户端证书，包括certCaContent，certCaName
listeners.n.certCaContent	否	String	上传客户端证书的内容，HTTPS监听器如果SSLMode=mutual，如果没有certCaId，则此项必传
listeners.n.certCaName	否	String	上传客户端CA证书的名称，HTTPS监听器如果SSLMode=mutual，如果没有certCaId，则此项必传。
listeners.n.certContent	否	String	上传服务端证书的内容，HTTPS监听器如果没有certId，则此项必传。
listeners.n.certKey	否	String	上传服务端证书的key，HTTPS监听器如果没有certId，则此项必传。
listeners.n.certName	否	String	上传服务端证书的名称，HTTPS监听器如果没有certId，则此项必传。

"""

loadBalancePorts = range(5000, 5010)
instancePorts = range(5000, 5010)

region = 'gz'
params = {
    'loadBalancerId': 'lb-7wes2ymbx',
}
for iIndex, iPort in enumerate(loadBalancePorts):
    params['listeners.' + '%d' % iIndex + '.loadBalancerPort'] = loadBalancePorts[iIndex]
    params['listeners.' + '%d' % iIndex + '.protocol'] = 2
    params['listeners.' + '%d' % iIndex + '.listenerName'] = 'listener_%d' % iPort
    params['listeners.' + '%d' % iIndex + '.instancePort'] = instancePorts[iIndex]

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
