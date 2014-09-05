import psutil
import time 
import datetime
import pygal

avg = 1


def create_timeseries(cpuint=1,percore=False ):
#    O(2^n)

    time_series = {}
    for i in range(10):
        cpu_load = psutil.cpu_times_percent(interval=cpuint, percpu=percore)
        datapoints = []
        for metric in cpu_load._fields:
            datapoints.append(getattr(cpu_load, metric))
            time_series.setdefault(metric, datapoints)

    return time_series
        

def create_graph(kpi_list):
    labels = []
    for label in kpi_list:
        labels.append(label)

    chart = pygal.Line()
    chart.x_labels = labels

    for line, serie in kpi_list.items():
        chart.add(line,serie)
    chart.render_to_file('chart.svg')
    

def main():
    kpis = create_timeseries(avg)
    create_graph(kpis)

if __name__ == '__main__':
    main()
