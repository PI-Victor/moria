import psutil
import time 
import datetime
import pygal
import random
from pygal.style import NeonStyle

avg = 1
sample = 10 

def create_timeseries(cpuint=1,percore=False):
#    O(2^n)
    time_series = {}

    for i in range(sample):
        datapoints = []
        cpu_load = psutil.cpu_times_percent(interval=cpuint, percpu=percore)
        [time_series.setdefault(metric,[]) for metric in cpu_load._fields]
        [v.append(getattr(cpu_load, k)) for k,v in time_series.items()]
#        [v.append(random.randrange(10)) for k,v in time_series.items()]   # for random quick testing of a graph
    return time_series

def create_graph(kpi_list):
    labels = []
    for label in kpi_list:
        labels.append(label)

    chart = pygal.StackedLine(fill=True,width=1024, height=600, style=NeonStyle)
    chart.x_labels = map(str, range(0,10))

    for line, series in kpi_list.items():
        chart.add(line,series)

    chart.render_to_file('chart.svg')
    

def main():
    while True:
        kpis = create_timeseries(avg)
        create_graph(kpis)

if __name__ == '__main__':
    main()
