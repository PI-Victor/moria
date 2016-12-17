import daemon
import signal
import lockfile

from kpigen.config import log, work_dir, log_fh, app_pid
from kpigen.metrics import CpuMetrics, VmMetrics
from kpigen.metrics import NetIoMetrics, DiskIoMetrics, SwapMetrics


def start_collection():
    log.info('Starting pooler...')
    while True:
        CpuMetrics().create_timeseries()
        VmMetrics().create_timeseries()
        SwapMetrics().create_timeseries()
        NetIoMetrics().create_timeseries()
        DiskIoMetrics().create_timeseries()

def cleanup():
    pass

def reload_config():
    pass

def main():
    ctx = daemon.DaemonContext(
        working_directory = work_dir,
        files_preserve = [log_fh.stream],
    )
    ctx.signal_map = {
        signal.SIGTERM: cleanup,
        signal.SIGHUP: 'terminate',
        signal.SIGUSR1: reload_config,
    }

    log.info('Starting daemon...')
    with ctx:
        start_collection()

if __name__ == '__main__':
    main()
