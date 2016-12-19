# -*- coding: utf-8 -*-
from abc import ABCMeta


class BackingService(object):
    __metaclass__ = ABCMeta
    self.uri = ''
    self.driver = ''

    def __init__(self):
        pass


class Service(object):
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
