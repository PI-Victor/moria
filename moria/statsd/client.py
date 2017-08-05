# -*- coding: utf-8 -*-
import statsd

from moria.blueprints.services import Service, BackingService
from moria.config import log

class StatsdClient(Service):
    def __init__(self, statsd):
        self._logger = log.getLogger(__name__)
        self.client = statsd.StatsClient(
                        statsd_host,
                        statsd_port,
                        prefix='moria',
                    )
        self.pipeline = self.client.pipeline()
    def connect(self):
        pass

    def start(self):
        pass

    def push(self):
        self.pipeline.gauge(entry, metric_value)
        self.pipeline.send()
