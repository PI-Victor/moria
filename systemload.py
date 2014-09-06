import psutil
import time 
import datetime
import pygal
import random

avg = 1
sample = 10 

def create_timeseries(cpuint=1,percore=False):
#    O(2^n)
    time_series = {}

    for i in range(sample):
        datapoints = []
        cpu_load = psutil.cpu_times_percent(interval=cpuint, percpu=percore)

        for metric in cpu_load._fields:
            time_series.setdefault(metric,[])
        
        for k,v in time_series.items():
            v = v.append(random.randrange(10))   # don't graph system load just generate randomly
#            v = v.append(getattr(cpu_load, k))

    return time_series

def create_graph(kpi_list):
    labels = []
    for label in kpi_list:
        labels.append(label)

    chart = pygal.Line()
    chart.x_labels = map(str, range(0,10))

    for line, series in kpi_list.items():
        chart.add(line,series)

    chart.render_to_file('chart.svg')
    

def main():
    kpis = create_timeseries(avg)
    create_graph(kpis)

if __name__ == '__main__':
    main()
