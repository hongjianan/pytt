# encoding: utf-8
'''
Created on 2018年4月20日

@author: Hong
'''

from oslo_config import cfg

'''
floats，booleans，list，dict，multi strings
'''
common_opts = [
	cfg.StrOpt('bind_host',
			default='0.0.0.0',
			help='IP address to listen on'),
	cfg.IntOpt('bind_port',
			default='1234',
			help='Port to listen on'),
]

cli_opts = [
	cfg.BoolOpt('debug',
			short='d',
			default=False,
			help='Print debug output'),
]

rabbit_group = cfg.OptGroup(name='rabbit',
                            title='RabbitMQ options')

rabbit_host_opt = cfg.StrOpt('host',
                             default='localhost',
                             help='IP/hostname to listen on')

rabbit_port_opt = cfg.IntOpt('port',
                            default=1234,
                            help='Port number to listen on')

conf = cfg.CONF

def cfg_tt():
	conf.register_cli_opts(cli_opts)


def group_cfg_tt():
	conf.register_group(rabbit_group)
	# options can be registered under a group in either of these ways:
	conf.register_opt(rabbit_host_opt, group=rabbit_group)
	conf.register_opt(rabbit_port_opt, group='rabbit')
	
	
	print(type(conf.rabbit.host), conf.rabbit.host)
	print(type(conf.rabbit.port), conf.rabbit.port, conf.rabbit.port)
	
if __name__ == '__main__':
# 	cfg_tt()
	group_cfg_tt()
	