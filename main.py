# -*- coding: utf-8 -*-
import click

from moria.config import log
from scheduler import start_services

@click.command()
@click.option('--master', default=False, help='Start as master.')
@click.option('--master-uri', default='', help='Master URI info for the slave \
node to send metrics data to.')
@click.option('--master-monitor', default=False, help='Start monitoring on \
the master node as well (default: disabled).')
@click.option('--bind-rest', default='127.0.0.1:8123', help='Bind master REST \
service to address.')
@click.option('--statsd', default='', help='Specify a StatsD instance to push \
data to.')
@click.option('--backing-service', default='', help='A backing service URI to \
store data. Currently supported (MongoDB, PostgresSQL, Redis)')
def start_services(master, master_uri, master_monitor, statsd, backing_service):
    if not master and master_uri=='':
        log.error('Attempting to start as slave without master URI info')
        return

    start_services(
        master,
        master_uri,
        master_monitor,
        bind_rest,
        statsd,
        backing_service,
    )

if __name__ == '__main__':
    start_services()
