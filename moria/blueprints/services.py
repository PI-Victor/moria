# -*- coding: utf-8 -*-
from abc import ABCMeta


class BackingServiceBlueprint(object):
    """Defines mandatory functionality for a backing service.
    """
    __metaclass__ = ABCMeta
    self.uri = ''
    self.driver = ''

    def __init__(self):
        pass


class ServicesBlueprint(object):
    """Defines mandatory functionality that a service should contain.
    """
    __metaclass__ = ABCMeta
    self.uri = ''
    self.logger = ''

    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def start(self):
        pass
