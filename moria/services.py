# -*- coding: utf-8 -*-
from abc import ABCMeta

class Service():
    __metaclass__ == ABCMeta
    self.uri = ''

    def __init__(self):
        pass


class Monitor(Service):
    def __init__(self):
        pass


class BackingService(Service):
    def __init__(self):
        pass


class RPCServer(Service):
    def __init__(self):
        pass


class RPCClient(Service):
    def __init__(self):
        pass


class RESTServer(Service):
    def __init__(self):
        pass
