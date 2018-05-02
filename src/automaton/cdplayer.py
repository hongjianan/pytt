# -*- coding: utf-8 -*-
'''
Created on 2018年4月16日

@author: Administrator
'''

from automaton import runners
from automaton import machines


def cb_on_enter(new_state, triggered_event):
    print('Enter:%s, event:%s' %(new_state, triggered_event))

def cb_on_exit(old_state, triggered_event):
    print('Exit:%s, event:%s' %(old_state, triggered_event))


class CDPlayer(object):
    def __init__(self):
        self.fsm = machines.FiniteMachine()
        self.define_state()
    
    def define_state(self):
        fsm = self.fsm
        fsm.add_state('closed', on_enter=cb_on_exit, on_exit=cb_on_enter)
        fsm.add_state('opened', on_enter=cb_on_exit, on_exit=cb_on_enter)
        fsm.add_state('playing', on_enter=cb_on_exit, on_exit=cb_on_enter)
        fsm.add_state('stopped', on_enter=cb_on_exit, on_exit=cb_on_enter)
        fsm.add_state('paused', on_enter=cb_on_exit, on_exit=cb_on_enter)
        
        fsm.default_start_state = 'closed'
        
#         fsm.add_transition(start, end, event, replace)

def player_tt():
    pass
    
if __name__ == '__main__':
    player_tt()
    