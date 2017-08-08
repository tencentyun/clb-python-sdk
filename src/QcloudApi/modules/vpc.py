#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Vpc(Base):
    requestHost = 'vpc.api.qcloud.com'

def main():
    action = 'DescribeSecurityGroups'
    config = {
        'Region': 'gz',
        'secretId': 'A***REMOVED***',
        'secretKey': '***REMOVED***',
        'method': 'get'
    }
    params = {}
    service = Vpc(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()
