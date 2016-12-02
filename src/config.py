import os
import logging

workdir = os.path.join(
    os.path.sep,
    os.path.dirname(os.path.realpath(__file__))
)
logfile = os.path.join(
            os.path.sep,
            workdir,
            'debug.log'
)
logging.basicConfig(
    filename=logfile,
    format='%(asctime)s %(levelname)s:%(message)s',
    filemode='a',
    level=logging.DEBUG,
)
graphdir = os.path.join(os.path.sep, work_dir, 'graphs')
log = logging.getLogger(__name__)
logfh = logging.FileHandler(logfile)
