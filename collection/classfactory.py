import time
import os
import psutil
import pygal
from pygal.style import NeonStyle
from mongoengine import connection, connect
from mongo_odm import CpuLoadDoc, VMemDoc, VSwapDoc, NetIoDoc, DiskIoDoc


work_dir = os.path.join(os.path.sep, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
graph_dir = os.path.join(os.path.sep, work_dir, 'graphs')


class BaseClass(object):
    def __init__(self):
        self.graph_fill = True
        self.graph_width = 1440
        self.graph_height = 500
        self.legend = True
    
    def create_timeseries(self, **kwargs):
        time_series = {}
        for point in range(self.sample):
            datapoints = []
            kpi_tuple = self.psfunct(**kwargs)
            [time_series.setdefault(metric,[]) for metric in kpi_tuple._fields]
            [values.append(getattr(kpi_tuple, metric)) for metric, values in time_series.items()]
            time.sleep(self.interval)
#        print time_series, self.document
        self.push_to_mongodb(time_series)
        self.create_graph(time_series)
        
    def push_to_mongodb(self, time_series):
        #leave this simple for now, try to access the db for the object, otherwise, return
        try:
            connect('kpidb')
        except connection.ConnectionError as e:
            print 'Conneciton to the db refused, running "on-the-fly mode", no history available'
            return 

        fields = [field for field in self.document._fields if (field != "id" and field != "timestamp")]
        for dbfield in self.document._meta_map:
            for datapoint in time_series:
                commit_fields =  '{}{}'.format(mapped, datapoint)
                print commit_fields

#        pushdocument = 
#        self.document.save(self.document(fields))
            
    def create_graph(self, kpi_list):
        labels = []
        for label in kpi_list:
            labels.append(label)
            chart = pygal.Line(fill=True, width=self.graph_width, height=self.graph_height, title=self.graph_tag, 
                               legend_at_bottom=self.legend)
            chart.x_labels = map(str, range(0,self.sample))
            for line, series in kpi_list.items():
#                print line, series # print the kpis to a file
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
        self.document = CpuLoadDoc
        super(CpuMetrics, self).__init__()

    def create_timeseries(self):
        super(CpuMetrics, self).create_timeseries(interval=self.interval, percpu=self.percpu)

    
class VmMetrics(BaseClass):
    def __init__(self, template='vmem.svg', graph_tag='Virtual Memory', sample=5, interval=5):
        self.message = 'Fetching Virtual Memory Metrics'
        self.template = template
        self.graph_tag = graph_tag
        self.sample = sample
        self.interval = interval
        self.psfunct = psutil.virtual_memory
        self.document = VMemDoc
        super(VmMetrics, self).__init__()

        
class SwapMetrics(BaseClass):
    def __init__(self, template='swap_mem.svg', graph_tag='Swap memory', sample=5, interval=5):
        self.message = 'Fetching Swap Memory Metrics'
        self.template = template
        self.graph_tag = graph_tag
        self.sample = sample
        self.interval = interval
        self.psfunct = psutil.swap_memory
        self.document = VSwapDoc
        super(SwapMetrics, self).__init__()


class NetIoMetrics(BaseClass):
    def __init__(self, template='netio.svg', graph_tag='Network IO', sample=5, interval=5):
        self.message = 'Fetching NIC Usage Metrics'
        self.template = template
        self.graph_tag = graph_tag
        self.sample = sample
        self.interval = interval
        self.psfunct = psutil.net_io_counters
        self.document = NetIoDoc
        super(NetIoMetrics, self).__init__()


class DiskIoMetrics(BaseClass):
    def __init__(self, template='diskio.svg', graph_tag='Diso IO Metrics', sample=5, interval=5):
        self.message = 'Fetching Disk IO'
        self.template = template
        self.graph_tag = graph_tag
        self.sample = sample
        self.interval = interval
        self.psfunct = psutil.disk_io_counters
        self.document = DiskIoDoc
        super(DiskIoMetrics, self).__init__()
