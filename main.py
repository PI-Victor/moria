"""
Something related to check out:
http://jsdatav.is/chap01.html
"""


import os
import sys
import logging
import daemon
from src.classfactory import CpuMetrics, VmMetrics
from src.classfactory import NetIoMetrics, DiskIoMetrics, SwapMetrics

# FIXME: move this to a config
work_dir = os.path.join(
    os.path.sep,
    os.path.dirname(os.path.realpath(__file__))
)
log_file = os.path.join(
            os.path.sep,
            work_dir,
            'debug.log'
)
logging.basicConfig(
    filename=log_file,
    format='%(asctime)s %(levelname)s:%(message)s',
    filemode='a',
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)

def load_functions():
    CpuMetrics().create_timeseries()
    VmMetrics().create_timeseries()
    SwapMetrics().create_timeseries()
    NetIoMetrics().create_timeseries()
    DiskIoMetrics().create_timeseries()

def main():

    ctx = daemon.DaemonContext(
        working_directory = work_dir,
        files_preserve = [log_handler],
        umask = 0o002,
    )
    with ctx:
        load_functions()

if __name__ == '__main__':
    main()
