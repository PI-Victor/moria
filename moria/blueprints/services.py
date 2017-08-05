# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class BackingServiceBlueprint(object):
    '''Defines mandatory functionality for a backing service.
    '''
    __metaclass__ = ABCMeta


class ServicesBlueprint(object):
    '''Defines mandatory functionality that a service should contain.
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def start(self):
        pass


class Service(ServicesBlueprint):
    '''Service defines the way that a service within the application should
    behave.
    '''

class BackingService(BackingServiceBlueprint):
    '''BackingService defines a way that a backing service within the
    application should behave.
    '''
