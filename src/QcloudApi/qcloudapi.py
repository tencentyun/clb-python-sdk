#!/usr/bin/python
# -*- coding: utf-8 -*-

config = {
    'Region':'gz',
    'secretId': '',
    'secretKey': '',
    'method': 'post'
}

class QcloudApi:
    def __init__(self, module='lb', config=config, region='gz'):
        config['Region'] = region
        self.module = module
        self.config = config

    def _factory(self, module, config):
        if (module == 'lb'):
            from modules.lb import Lb
            service = Lb(config)
        else:
            raise ValueError , 'module not exists'

        return service

    def setSecretId(self, secretId):
        self.config['secretId'] = secretId

    def setSecretKey(self, secretKey):
        self.config['secretKey'] = secretKey

    def setRequestMethod(self, method):
        self.config['method'] = method

    def setRegion(self, region):
        self.config['region'] = region

    def generateUrl(self, action, params):
        service = self._factory(self.module, self.config)
        return service.generateUrl(action, params)

    def call(self, action, params):
        service = self._factory(self.module, self.config)

        methods = dir(service)
        for method in methods:
            if (method == action):
                func = getattr(service, action)
                return func(params)

        return service.call(action, params)
