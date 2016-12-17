# -*- coding: utf-8 -*-
import os
import logging

work_dir = os.path.join(
    os.path.sep,
    os.path.dirname(os.path.dirname(
                    os.path.realpath(__file__))
                    )
)
log_file = os.path.join(
            os.path.sep,
            work_dir,
            'debug.log'
)
logging.basicConfig(
    filename=log_file,
    format='%(asctime)s %(levelname)s:%(message)s',
    filemode='a',
    level=logging.DEBUG,
)
log = logging.getLogger(__name__)
log_fh = logging.FileHandler(log_file)
log.addHandler(log_fh)
