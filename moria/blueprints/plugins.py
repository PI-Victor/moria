# -*- coding: utf-8 -*-
from abc import ABCMeta


class PluginsBlueprint(object):
    __metaclass__ = ABCMeta

    def start_scheduler(self, interval, samples):
        """This schedules pooling of metrics
        """
        pass

    def export_resources(self):
        """Returns a Flask RESTful resource dictionary that is used by the
        RestServer to load endpoints.
        """
        pass
