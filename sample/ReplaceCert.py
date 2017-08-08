#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from src.QcloudApi.qcloudapi import QcloudApi
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

action = 'ReplaceCert'  # 替换证书

"""
oldCertId	必传 要被更换的证书ID，可以是服务端证书ID，也可以是客户端证书ID。
newCertId	非必传	新的证书ID,若此项不填，则newCertContent，newCertName必填，此外若是服务端证书，newCertKey必填。
newCertContent	非必传	新的证书内容，如果没有此项，则newCertId必填。
newCertName	非必传	新的证书名称，如果没有此项，则newCertId必填。
newCertKey	非必传	新的证书私钥,服务端证书如果没有没有此项，则newCertId必填。

"""
region = 'gz'
params = {
    'oldCertId': "9AH5hrPf",
    # 'newCertId':"9945e3e3",
    'newCertContent': '''-----BEGIN CERTIFICATE-----

        -----END CERTIFICATE-----
    ''',
    'newCertKey': """-----BEGIN RSA PRIVATE KEY-----
    """,
    'newCertName': "cert",
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
