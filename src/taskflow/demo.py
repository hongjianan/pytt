# -*- coding: utf-8 -*-
'''
Created on 2018年5月4日

@author: Administrator
'''

from taskflow.patterns import linear_flow as lt
from taskflow import task, engines
from taskflow.types import failure as task_failed


class CallJim(task.Task):

    default_provides = set(['jim_new_number'])

    def execute(self, jim_number, *args, **kwargs):
        print "Calling Jim %s." % jim_number
        print '=' * 10
        jim_new_number = jim_number + 'new'

        return {'jim_new_number': jim_new_number}

    def revert(self, result, *args, **kwargs):
        if isinstance(result, task_failed.Failure):
            print "jim result"
            return None

        jim_new_number = result['jim_new_number']
        print "Calling jim %s and apologizing." % jim_new_number


class CallJoe(task.Task):

    default_provides = set(['joe_new_number', 'jim_new_number'])

    def execute(self, joe_number, jim_new_number, *args, **kwargs):
        print "Calling jim %s." % jim_new_number
        print "Calling Joe %s." % joe_number
        print '=' * 10
        joe_new_number = joe_number + 'new'

        return {'jim_new_number': jim_new_number,
                'joe_new_number': joe_new_number}

    def revert(self, result, *args, **kwargs):
        if isinstance(result, task_failed.Failure):
            print "joe result"
            return None

        jim_new_number = result['jim_new_number']
        joe_new_number = result['joe_new_number']

        print "Calling joe %s and apologizing." % joe_new_number


class CallJmilkFan(task.Task):

    default_provides = set(['new_numbers'])

    def execute(self, jim_new_number, joe_new_number, jmilkfan_number,
                *args, **kwargs):
        print "Calling jim %s" % jim_new_number
        print "Calling joe %s" % joe_new_number
        print "Calling jmilkfan %s" % jmilkfan_number
        print '=' * 10
        jmilkfan_new_number = jmilkfan_number + 'new'

        raise ValueError('Error')
        new_numbers =  {'jim_new_number': jim_new_number,
                        'joe_new_number': joe_new_number,
                        'jmilkfan_new_number': jmilkfan_new_number}

        return {'new_numbers': new_numbers}

    def revert(self, result, *args, **kwargs):
        if isinstance(result, task_failed.Failure):
            print "jmilkfan result"
            return None

        jim_new_number = result['jim_new_number']
        joe_new_number = result['joe_new_number']
        jmilkfan_new_number = result['jmilkfan_new_number']

        print "Calling jmilkfan %s and apologizing." % jmilkfan_new_number


def get_flow(flow, numbers):
    flow_name = flow
    flow_api = lt.Flow(flow_name)

    flow_api.add(CallJim(),
                 CallJoe(),
                 CallJmilkFan())

    return engines.load(flow_api,
                                 engine_conf={'engine': 'serial'},
                                 store=numbers)

def demo():
    numbers = {'jim_number': '1'*6,
               'joe_number': '2'*6,
               'jmilkfan_number': '3'*6}
    try:
        flow_engine = get_flow(flow='taskflow-demo',
                               numbers=numbers)

        flow_engine.run()
    except Exception:
        print "TaskFlow Failed!"
    else:
        new_numbers = flow_engine.storage.fetch('new_numbers')


def man_run():
    task = CallJim()
    task.execute('1234')

if __name__ == '__main__':
#     demo()
    man_run()

