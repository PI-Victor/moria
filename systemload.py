import psutil
import time 
import datetime
import pygal
import random
from pygal.style import NeonStyle
import daemon
import logging
import os

avg = 1
sample = 10 

debug_log = os.path.join(os.path.sep, os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'debug.log')

logging.basicConfig(filename=debug_log, format='%(asctime)s %(levelname)s:%(messages)s',
                    filemode='a', level=logging.DEBUG)

def create_timeseries(kpi_tuple):
    time_series = {}
    for point in range(sample):
        datapoints = []
        [time_series.setdefault(metric,[]) for metric in kpi_tuple._fields]
        [values.append(getattr(kpi_tuple, metric)) for metric,values in time_series.items()]
    return time_series

def cpu_metrics():
    cpuload_tuple = psutil.cpu_times_percent(interval=avg, percpu=False)
    time_series = create_timeseries(cpuload_tuple)
    print time_series

def vmem_metrics():
    vmem_tuple = psutil.virtual_memory()
    time_series = create_timeseries(vmem_tuple)
    print time_series

def swapmem_metrics():
    swapmem_tuple = psutil.swap_memory()
    time_series = create_timeseries(swapmem_tuple)
    print time_series

def create_graph(kpi_list, chart_name='chart.svg'):
    labels = []
    for label in kpi_list:
        labels.append(label)
    chart = pygal.Line(fill=True,width=1024, height=600, style=NeonStyle)
    chart.x_labels = map(str, range(0,10))
    for line, series in kpi_list.items():
        print line, series
        chart.add(line,series)
    chart.render_to_file(chart_name)

def main():
    cpu_metrics()
    vmem_metrics()
    swapmem_metrics()

if __name__ == '__main__':
    main()
