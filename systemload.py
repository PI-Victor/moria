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
debug_log = os.path.join(os.path.sep, work_dir, 'debug.log')
logging.basicConfig(
    filename=debug_log,
    format='%(asctime)s %(levelname)s:%(message)s',
    filemode='a', level=logging.DEBUG
)


def load_functions():
    CpuMetrics().create_timeseries()
    VmMetrics().create_timeseries()
    SwapMetrics().create_timeseries()
    NetIoMetrics().create_timeseries()
    DiskIoMetrics().create_timeseries()

def main():
    daemon_context = daemon.DaemonContext(
        files_preserve = [logging.FileHandler(debug_log)]
    )
    with daemon_context:
        load_functions()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sample = 15 #how many sample to currently grab for each graph
        print 'You can send the number of samples, as a parameter, needed for the graphs, default is 15'
    else:
        try:
            sample = int(sys.argv[1])
        except ValueError:
            print "That's not an integer, reverting to default 15 samples"
            sample = 15
    main()
