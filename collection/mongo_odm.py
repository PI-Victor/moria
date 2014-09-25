from mongoengine import *  
import datetime


class CpuLoadDoc(Document):
    timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow())
    cpu_softirq = FloatField()
    cpu_iowait = FloatField()
    cpu_sys = FloatField()
    cpu_guest = FloatField()
    cpu_idle = FloatField()
    cpu_user = FloatField()
    cpu_guestnice = FloatField()
    cpu_irq = FloatField()
    cpu_steal = FloatField()
    cpu_nice = FloatField()
    
    _meta_map = {'softirq' : 'cpu_softirq',
                 'iowait': 'cpu_iowait',
                 'system': 'cpu_sys',
                 'guest': 'cpu_guest',
                 'idle': 'cpu_idle',
                 'user': 'cpu_user',
                 'guest_nice': 'cpu_guestnice',
                 'irq': 'cpu_irq',
                 'steal': 'cpu_steal',
                 'nice': 'cpu_nice'
    }

class VMemDoc(Document):
    timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow())
    vm_total = IntField()
    vm_used = IntField()
    vm_cached = IntField()
    vm_percent = FloatField()
    vm_free = IntField()
    vm_inactive = IntField()
    vm_active = IntField()
    vm_available = IntField()
    vm_buffers = IntField()


class VSwapDoc(Document):
    timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow())
    vs_used = IntField()
    vs_percent = FloatField()
    vs_free = IntField()
    vs_sout = IntField()
    vs_total = IntField()
    vs_sin = IntField()


class NetIoDoc(Document):
    timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow())
    net_packsent = IntField()
    net_bytrecv = IntField()
    net_packrecv = IntField()
    net_droping = IntField()
    net_dropout = IntField()
    net_bytsent = IntField()
    net_errout = IntField()
    net_errin = IntField()


class DiskIoDoc(Document):
    timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow())
    disk_writebyt = IntField()
    disk_readcount = IntField()
    disk_writecount = IntField()
    disk_readtime = IntField()
    disk_readbyt = IntField()
    disk_writebyt = IntField()
