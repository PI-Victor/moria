import time
import os
import psutil
import pygal
from pygal.style import NeonStyle

work_dir = os.path.join(os.path.sep, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
graph_dir = os.path.join(os.path.sep, work_dir, 'graphs')


class BaseClass(object):
    def __init__(self):
        self.graph_fill = True
        self.graph_width = 1440
        self.graph_height = 500
        self.legend = True
    
    def create_timeseries(self, *args):
        time_series = {}
        for point in range(self.sample):
            datapoints = []
            kpi_tuple = self.psfunct(*args)
            [time_series.setdefault(metric,[]) for metric in kpi_tuple._fields]
            [values.append(getattr(kpi_tuple, metric)) for metric, values in time_series.items()]
            time.sleep(self.interval)
        self.create_graph(time_series)

    def create_graph(self, kpi_list):
        labels = []
        for label in kpi_list:
            labels.append(label)
            chart = pygal.Line(fill=True, width=self.graph_width, height=self.graph_height, title=self.graph_tag, 
                               legend_at_bottom=self.legend)
            chart.x_labels = map(str, range(0,self.sample))
            for line, series in kpi_list.items():
                chart.add(line,series)
            chart.render_to_file(os.path.join(os.path.sep, graph_dir, self.template))


class CpuMetrics(BaseClass):
    def __init__(self, template='cpu_load.svg', graph_tag='Cpu Load Total', sample=5, interval=1):
        self.message = 'Cpu Processing started'
        self.template = template
        self.graph_tag = graph_tag
        self.psfunct = psutil.cpu_times_percent
        self.sample = sample
        self.interval = interval
        self.percpu = False
        super(CpuMetrics, self).__init__()

    def create_timeseries(self):
        super(CpuMetrics, self).create_timeseries(self.interval, self.percpu)

    
class VmMetrics(BaseClass):
    def __init__(self, template='vmem.svg', graph_tag='Virtual Memory', sample=5, interval=5):
        self.message = 'Fetching Virtual Memory Metrics'
        self.template = template
        self.graph_tag = graph_tag
        self.sample = sample
        self.interval = interval
        self.psfunct = psutil.virtual_memory
        super(VmMetrics, self).__init__()

        
class SwapMetrics(BaseClass):
    def __init__(self, template='swap_mem.svg', graph_tag='Swap memory', sample=5, interval=5):
        self.message = 'Fetching Swap Memory Metrics'
        self.template = template
        self.graph_tag = graph_tag
        self.sample = sample
        self.interval = interval
        self.psfunct = psutil.swap_memory
        super(SwapMetrics, self).__init__()


class NetIoMetrics(BaseClass):
    def __init__(self, template='netio.svg', graph_tag='Network IO', sample=5, interval=5):
        self.message = 'Fetching NIC Usage Metrics'
        self.template = template
        self.graph_tag = graph_tag
        self.sample = sample
        self.interval = interval
        self.psfunct = psutil.net_io_counters
        super(NetIoMetrics, self).__init__()

class DiskIoMetrics(BaseClass):
    def __init__(self, template='diskio.svg', graph_tag='Diso IO Metrics', sample=5, interval=5):
        self.message = 'Fetching Disk IO'
        self.template = template
        self.graph_tag = graph_tag
        self.sample = sample
        self.interval = interval
        self.psfunct = psutil.disk_io_counters
        super(DiskIoMetrics, self).__init__()
