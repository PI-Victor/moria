import os
import sys

from collection.classfactory import CpuMetrics, VmMetrics, NetIoMetrics, DiskIoMetrics, SwapMetrics

import daemon
import logging

'''TODO : Must implement multiproc and a daemon for precise computation of system usage
execution is sequential at this point, and the sample parameter delays data for the
next time series
'''

if len(sys.argv) < 2:
    sample = 15 #how many sample to currently grab for each graph
    print 'You can send the number of samples, as a parameter, needed for the graphs, default is 15'
else:
    try:
        sample = int(sys.argv[1])
    except ValueError:
        print "That's not an integer, reverting to default 15 samples"
        sample = 15

avg = 1 #time to sample cpu usage
work_dir = os.path.join(os.path.sep, os.path.dirname(os.path.realpath(__file__)))
debug_log = os.path.join(os.path.sep, work_dir, 'debug.log')
graph_dir = os.path.join(os.path.sep, work_dir, 'graphs')

logging.basicConfig(filename=debug_log, format='%(asctime)s %(levelname)s:%(message)s',
                    filemode='a', level=logging.DEBUG)

def main():
    daemon_context = daemon.DaemonContext(files_preserve = [logging.FileHandler(debug_log)])
    #with daemon_context:
    while True:
        CpuMetrics().create_timeseries()
        VmMetrics().create_timeseries()
        SwapMetrics().create_timeseries()
        NetIoMetrics().create_timeseries()
        DiskIoMetrics().create_timeseries()
            
if __name__ == '__main__':
    main()
