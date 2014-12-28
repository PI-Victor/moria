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
        self.time_series = {}
        for point in range(self.sample):
            datapoints = []
            kpi_tuple = self.psfunct(**kwargs)
            [self.time_series.setdefault(metric,[]) for metric in kpi_tuple._fields]
            [values.append(getattr(kpi_tuple, metric)) for metric, values in self.time_series.items()]
            time.sleep(self.interval)
        self.push_to_mongodb()
        self.create_graph(self.time_series)

        
    def push_to_mongodb(self):
        #leave this simple for now, try to access the db for the object, otherwise, return
        try:
            connect('kpidb')
            print "Connection accepted, pushing to mongo database: 'kpidb' "
            print self.message
        except connection.ConnectionError as e:
            print 'Connection to the db refused, running "on-the-fly mode", no history available'
            return 

        
#        commit_fields = ''
#        for dbfield, mapped in self.document._meta_map.items():
#            for datapoint in time_series:
#                if datapoint == dbfield:
#                    print time_series[datapoint]
#                    commit_fields =  "{}, {} = {}".format(commit_fields, mapped, time_series[datapoint])
        
#        self.document.save(pushdocument)


    def create_graph(self, kpi_list):
        labels = []
        for label in kpi_list:
            labels.append(label)
            chart = pygal.Line(fill=True, width=self.graph_width, height=self.graph_height, title=self.graph_tag, 
                               legend_at_bottom=self.legend)
            chart.x_labels = map(str, range(0, self.sample))
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
        self.document = CpuLoadDoc
        super(CpuMetrics, self).__init__()

        
    def create_timeseries(self):
        super(CpuMetrics, self).create_timeseries(interval=self.interval, percpu=self.percpu)

        
    def push_to_mongodb(self):
        super(CpuMetrics, self).push_to_mongodb()
        #this triggers my OCD, but i can't find a better solution for inserting values in the db
        #at this point, will leave it as it is, until i figure it out. boooo!
        cpuloaddoc = self.document(
            cpu_softirq = self.time_series['softirq'],
            cpu_iowait = self.time_series['iowait'],
            cpu_sys = self.time_series['system'],
            cpu_guest = self.time_series['guest'],
            cpu_idle = self.time_series['idle'],
            cpu_user = self.time_series['user'],
            cpu_guestnice = self.time_series['guest_nice'],
            cpu_irq = self.time_series['irq'],
            cpu_steal = self.time_series['steal'],
            cpu_nice = self.time_series['nice'],
        )
        cpuloaddoc.save()
    
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

        
    def push_to_mongodb(self):
        super(VmMetrics, self).push_to_mongodb()
        vmdoc = self.document(
            vm_total = self.time_series['total'],
            vm_available = self.time_series['available'],
            vm_percent = self.time_series['percent'],
            vm_used = self.time_series['used'],
            vm_free = self.time_series['free'],
            vm_active = self.time_series['active'],
            vm_inactive = self.time_series['inactive'],
            vm_buffers = self.time_series['buffers'],
            vm_cached = self.time_series['cached'],
        )
        vmdoc.save()

        
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

        
    def push_to_mongodb(self):
        super(SwapMetrics, self).push_to_mongodb()
        vswapdoc = self.document(
            vs_used = self.time_series['used'],
            vs_total = self.time_series['total'],
            vs_free = self.time_series['free'],
            vs_percent = self.time_series['percent'],
            vs_sin = self.time_series['sin'],
            vs_sout = self.time_series['sout'],
        )
        vswapdoc.save()


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

        
    def push_to_mongodb(self):
        super(NetIoMetrics, self).push_to_mongodb()
        netiodoc = self.document(
            net_packsent = self.time_series['packets_sent'],
            net_bytrecv = self.time_series['bytes_recv'],
            net_packrecv = self.time_series['packets_recv'],
            net_dropin = self.time_series['dropin'],
            net_dropout = self.time_series['dropout'],
            net_bytsent = self.time_series['bytes_sent'],
            net_errout = self.time_series['errout'],
            net_errin = self.time_series['errin'],
        )
        netiodoc.save()

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

        
    def push_to_mongodb(self):
        super(DiskIoMetrics, self).push_to_mongodb()
        diskiodoc = self.document(
            disk_writebyte = self.time_series['write_bytes'],
            disk_readcount = self.time_series['read_count'],
            disk_writecount = self.time_series['write_count'],
            disk_readtime = self.time_series['read_time'],
            disk_readbyte = self.time_series['read_bytes'],
            disk_writetime = self.time_series['write_time'],
        )
        diskiodoc.save()
