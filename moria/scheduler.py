# -*- coding: utf-8 -*-
import os

from rest.server import RESTServer
from statsd.client import StatsdClient
from rpc.server import RPCServer
from rpc.client import RPCClient
from config import work_dir


def start_services(
    master,
    master_uri,
    master_monitor,
    bind_rest,
    statsd,
    backing_service,
):
    if not master:
        start_node_services(master_uri)
    else:
        start_master_services(
            master_monitor,
            bind_rest,
            statsd,
            backing_service,
        )

def start_master_services(master_monitor, bind_rest, statsd, backing_service):
    start_rest_service(bind_rest)

def start_node_services(master_uri):
    pass

def service_scheduler():
    pass

def start_rest_service():
    plugins = load_plugins()
    rest = RESTServer(bind_rest, plugins)

def load_plugins():
    plugins_dir = os.join(work_dir, 'moria', 'plugins')


class ServiceScheduler(object):
    def __init__(self):
        self._service_queue = ''

    def add_service_to_queue(self):
        pass

    def remove_service_from_queue(self):
        pass
