from mongoengine import *  
import datetime


class CpuLoadDoc(Document):
    timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow())
    cpu_softirq = ListField()
    cpu_iowait = ListField()
    cpu_sys = ListField()
    cpu_guest = ListField()
    cpu_idle = ListField()
    cpu_user = ListField()
    cpu_guestnice = ListField()
    cpu_irq = ListField()
    cpu_steal = ListField()
    cpu_nice = ListField()
    
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
    vm_total = ListField()
    vm_used = ListField()
    vm_cached = ListField()
    vm_percent = ListField()
    vm_free = ListField()
    vm_inactive = ListField()
    vm_active = ListField()
    vm_available = ListField()
    vm_buffers = ListField()
    
    _meta_map = {''}


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
