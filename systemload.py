import psutil
import time 
import datetime
import pygal

avg = 1


def create_timeseries(cpuint=1,percore=False ):
    time_series = {}
    cpu_load = psutil.cpu_times_percent(interval=cpuint, percpu=percore)
    
    for metric in cpu_load._fields:
        time_series.setdefault(metric,getattr(cpu_load, metric))
    
    return time_series
        

def create_graph(kpi_list):
    for label in kpi_list:
        labels = 

    chart = pygal.Line()
    chart.x_labels = [
        'test1',
        'test2',
        'test3',
    ]
#    chart.add(kpi_list)
#    chart.render()
    

def main():
    while True:
        kpis = create_timeseries(avg)
        create_graph(kpis)

if __name__ == '__main__':
    main()
