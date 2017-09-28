#!/usr/bin/python
# -*- coding: utf-8 -*-

from base import Base

class Dfw(Base):
    requestHost = 'dfw.api.qcloud.com'

def main():
    action = 'DescribeSecurityGroups'
    config = {
        'Region': 'gz',
        'secretId': 'ÄãµÄsecretId',
        'secretKey': 'ÄãµÄsecretKey',
        'method': 'get'
    }
    params = {}
    service = Dfw(config)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()