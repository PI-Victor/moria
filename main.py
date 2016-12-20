import click

from moria.config import log


@click.command()
@click.option('--master', default=False, help='Start app as master node.')
@click.option('--master-uri', default='', help='Master URI info')
@click.option('--master-monitor', default=False, help='Start monitoring on the \
master node as well. Disabled by default')
@click.option('--bind-rest', default='127.0.0.1:8123', help='Bind REST service \
to address')
@click.option('--statsd', default='', help='StasD URI info')
def start_services(master, master_uri, master_monitor, statsd):
    if not master and master_uri=='':
        log.error('Attempting to start as slave without master URI info')
        return

    if master:
        log.Info('Starting node in master mode')
        return

if __name__ == '__main__':
    start_services()
