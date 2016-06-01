# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import json
import threading
import six
from twisted.logger import formatEvent, globalLogPublisher
from kafka import KafkaProducer

lock = threading.RLock()
level_mapping = {
    'debug': 'DEBUG',
    'info': 'INFO',
    'warn': 'WARNING',
    'error': 'ERROR',
    'critical': 'CRITICAL'
}

def kafka_observer(event):
    message = formatEvent(event)
    event_dict = dict()
    for slot in ['log_logger', 'log_source', 'log_failure']:
        if slot in event:
            event_dict[slot] = repr(event[slot])
    event_dict['log_level'] = event['log_level'].name
    for slot in six.iterkeys(event):
        
