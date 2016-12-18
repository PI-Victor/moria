# -*- coding: utf-8 -*-
from abc import ABCMeta

class Service():
    __metaclass__ = ABCMeta
    self.uri = ''
    self.logger = ''

    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def bind(self, address):
        pass

    @abstractmethod
    def start(self):
        pass


class Monitor(Service):
    def __init__(self):
        pass

    def connect(self):
        pass

    def bind(self, address):
        pass

    def start(self):
        pass


class BackingService(Service):
    def __init__(self):
        pass

    def connect(self):
        pass

    def bind(self, address):
        pass

    def start(self):
        pass


class RPCServer(Service):
    def __init__(self):
        pass

    def connect(self):
        pass

    def bind(self, address):
        pass

    def start(self):
        pass


class RPCClient(Service):
    def __init__(self):
        pass

    def connect(self):
        pass

    def bind(self, address):
        pass

    def start(self):
        pass


class RESTServer(Service):
    def __init__(self):
        pass

    def connect(self):
        pass

    def bind(self, address):
        pass

    def start(self):
        pass
