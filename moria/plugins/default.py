# -*- coding: utf-8 -*-
import psutil

from blueprints.plugins import PluginsBlueprint


class DefaultPlugin(PluginsBlueprint):
    def __init__(self):
        self.platform = ''

    def start_scheduler(self):
        pass
        
    def export_resources(self):
        pass
