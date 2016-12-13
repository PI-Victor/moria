import daemon
import signal
import lockfile

from kpigenerator.config import log, workdir, logfh
from kpigenerator.metrics import CpuMetrics, VmMetrics
from kpigenerator.metrics import NetIoMetrics, DiskIoMetrics, SwapMetrics

def load_functions():
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
        working_directory = workdir,
        files_preserve = [logfh],
        umask = 0o002,
        pidfile=lockfile.FileLock('/var/run/spam.pid'),
    )
    ctx.signal_map = {
        signal.SIGTERM: cleanup,
        signal.SIGHUP: 'terminate',
        signal.SIGUSR1: reload_config,
    }

    log.info('Loading metrics...')
    with ctx:
        load_functions()

if __name__ == '__main__':
    main()
