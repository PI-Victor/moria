# -*- coding: utf-8 -*-
from mongoengine import *
import datetime


class CpuLoadDoc(Document):
    timestamp = DateTimeField(
        required=True,
        default=datetime.datetime.utcnow(),
    )
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

    _meta_map = {
        'softirq' : 'cpu_softirq',
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


class VSwapDoc(Document):
    timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow())
    vs_used = ListField()
    vs_percent = ListField()
    vs_free = ListField()
    vs_sout = ListField()
    vs_total = ListField()
    vs_sin = ListField()


class NetIoDoc(Document):
    timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow())
    net_packsent = ListField()
    net_bytrecv = ListField()
    net_packrecv = ListField()
    net_dropin = ListField()
    net_dropout = ListField()
    net_bytsent = ListField()
    net_errout = ListField()
    net_errin = ListField()


class DiskIoDoc(Document):
    timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow())
    disk_writebyte = ListField()
    disk_readcount = ListField()
    disk_writecount = ListField()
    disk_readtime = ListField()
    disk_readbyte = ListField()
    disk_writetime = ListField()
