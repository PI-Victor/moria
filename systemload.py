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

work_dir = os.path.join(os.path.sep, os.path.dirname(os.path.realpath(__file__)))
debug_log = os.path.join(os.path.sep, work_dir, 'debug.log')
graph_dir = os.path.join(os.path.sep, work_dir, 'graphs')

logging.basicConfig(filename=debug_log, format='%(asctime)s %(levelname)s:%(message)s',
                    filemode='a', level=logging.DEBUG)


def create_timeseries(psfunct, *args):
    time_series = {}
    for point in range(sample):
        datapoints = []
        kpi_tuple = psfunct(*args)
        [time_series.setdefault(metric,[]) for metric in kpi_tuple._fields]
        [values.append(getattr(kpi_tuple, metric)) for metric,values in time_series.items()]
    return time_series

def cpu_metrics():
    logging.debug('Fetching Cpu Load metrics')
    cpuload_funct = psutil.cpu_times_percent 
    interval=avg 
    percpu=False
    metric_sample = create_timeseries(cpuload_funct, interval, percpu)
    create_graph(metric_sample, 'cpu_load.svg', 'Cpu Load')

def vmem_metrics():
    logging.debug('Fetching Virtual Memory metrics')
    vmem_funct = psutil.virtual_memory
    metric_sample = create_timeseries(vmem_funct)
    create_graph(metric_sample, 'vmem.svg', 'Virtual Memory')

def swapmem_metrics():
    logging.debug('Fetching Swap Memory metrics')
    swapmem_funct = psutil.swap_memory
    metric_sample = create_timeseries(swapmem_funct)
    create_graph(metric_sample,'swap_mem.svg','Swap Memory')

def create_graph(kpi_list, chart_name='chart.svg', chart_title='default'):
    labels = []
    for label in kpi_list:
        labels.append(label)
    chart = pygal.StackedLine(fill=True, width=1024, height=600, title=chart_title, 
                      legend_at_bottom=True)
    chart.x_labels = map(str, range(0,10))
    for line, series in kpi_list.items():
        chart.add(line,series)
    chart.render_to_file(os.path.join(os.path.sep, graph_dir, chart_name))

def main():
    #logging.FileHandler()
    while True:
        cpu_metrics()
        vmem_metrics()
        swapmem_metrics()
        
if __name__ == '__main__':
    main()
