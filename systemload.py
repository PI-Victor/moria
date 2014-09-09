import psutil
import time 
import datetime
import pygal
import random
from pygal.style import NeonStyle

avg = 1
sample = 10 

def create_timeseries(kpi_tuple):
    time_series = {}
    for point in range(sample):
        datapoints = []
        [time_series.setdefault(metric,[]) for metric in kpi_tuple._fields]
        [values.append(getattr(cpu_load, metric)) for metric,values in time_series.items()]
    return time_series

def get_cpu_metrics():
    cpuload_tuple = psutil.cpu_times_percent(interval=cpuint, percpu=percore)
    time_series = create_timeseries(cpuload_tuple)
    print time_series

def get_vmem_metrics():
    vmem_tuple = psutil.virtual_memory()
    time_series = create_timeseries(vmem_tuple)
    print time_series

def swap_memory():
    swapmem_tuple = psutil.swap_memory()
    time_series = create_timeseries(swapmem_tuple)
    print time_series

def create_graph(kpi_list):
    labels = []
    for label in kpi_list:
        labels.append(label)
    chart = pygal.StackedLine(fill=True,width=1024, height=600, style=NeonStyle)
    chart.x_labels = map(str, range(0,10))
    for line, series in kpi_list.items():
        print line, series
        chart.add(line,series)
    chart.render_to_file('chart.svg')


def main():
    while True:


if __name__ == '__main__':
    main()
