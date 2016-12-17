# -*- coding: utf-8 -*-
class Metric(object):
    def __init__(self):
        pass


class MetricsBucket(object):
    """ Generic class for metric buckets
    """
    def __init__(self):
        pass

    def __iter__(self):
        pass


class Gauge(Metric):
    def __init__(self):
        pass


class Counter(Metric):
    def __init__(self):
        pass


class Timer(Metric):
    def __init__(self):
        pass


class Sample(Metric):
    def __init__(self):
        pass


class MultiMetric(Metric, MetricsBucket):
    def __init__(self):
        pass
