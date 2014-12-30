"""Author: https://github.com/PI-Victor
This project has no purpose but the learning mongodb, mongoengine, pygal
and the handling of Data series events, metrics and KPIs

The MIT License (MIT)
Copyright (c)
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

"""Something related to check out:
http://jsdatav.is/chap01.html
"""


import os
import sys
import logging
import daemon
from collection.classfactory import CpuMetrics, VmMetrics
from collection.classfactory import NetIoMetrics, DiskIoMetrics, SwapMetrics

#TODO : Must implement multiproc and a daemon for precise computation of system usage
#execution is sequential at this point, and the sample parameter delays data for the
#next time series
work_dir = os.path.join(os.path.sep, os.path.dirname(os.path.realpath(__file__)))
debug_log = os.path.join(os.path.sep, work_dir, 'debug.log')
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
