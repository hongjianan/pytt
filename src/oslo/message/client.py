# encoding: UTF-8
'''
Created on 2018年4月19日

@author: jason
'''

import oslo_messaging as messaging
from oslo_context import context
from oslo_config import cfg
from oslo_log import log as logging

CONF = cfg.CONF
LOG = logging.getLogger(__name__)
logging.register_options(CONF)
logging.setup(CONF, "myservice")
CONF(default_config_files=['app.conf'])


def client():
    ctxt = {}
    arg = {'a':'b'}
    transport = messaging.get_transport(CONF)
    target = messaging.Target(topic='test123')
    client = messaging.RPCClient(transport, target)
    client.call(ctxt, 'test', arg=arg)

if __name__ == '__main__':
    pass