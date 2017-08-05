# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api, Resource

from moria.blueprints.services import Service, BackingService
from moria.config import log


class RESTServer(Service):
    def __init__(self, bind_address, plugins):
        self.logger = log.getLogger(__name__)
        self._api_resources = resource_map

        self._app = Flask('moria')
        self._api = Api(app)

        load_resources(api)
        self.start(bind_address)

    def connect(self):
        pass

    def start(self, bind_address):
        app.run(self._app)

    def load_resources(self, api):
        for resource, path in self._api_resources:
            api.add_resource(resource, path)
