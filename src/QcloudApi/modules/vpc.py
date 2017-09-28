#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Vpc(Base):
    requestHost = 'vpc.api.qcloud.com'

def main():
    action = 'DescribeSecurityGroups'
    config = {
        'Region': 'gz',
        'secretId': 'ÄãµÄsecretId',
        'secretKey': 'ÄãµÄsecretKey',
        'method': 'get'
    }
    params = {}
    service = Vpc(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()
