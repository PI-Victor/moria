# -*- coding: utf-8 -*-
from moria.services import Service, BackingService


class Monitor(Service):
    """Monitor is the service that manages pooling of metrics based on the
    plugin system.
    """

    def __init__(self, interval):
        self.interval = interval

    def connect(self):
        return False

    def bind(self, address):
        pass

    def start(self):
        while True:
            run_pooler()

    def run_pooler(self):
        pass


class PoolScheduler(object):
    """PoolScheduler handles the scheduling of pooling metrics.
    """
    def __init__(self):
        self._pool_objects = []


class MetricsBucket(object):
    """MetricsBucket is the JSON representation of a metrics snapshot at a
    point in time.
    """
    def __init__(self):
        pass
