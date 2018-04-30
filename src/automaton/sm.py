# -*- coding: utf-8 -*-
'''
Created on 2018年4月16日

@author: Administrator
'''

# import automaton
from automaton import machines
from automaton import runners


class SwitchState():
    def __init__(self):
        self.fsm = machines.FiniteMachine()
        self.define_state()
    
    def __repr__(self):
        return self.fsm.pformat()
      
    def define_state(self):
        self.fsm.add_state('Y')
        self.fsm.add_state('N')
        self.fsm.add_transition('Y', 'N', 'close')
        self.fsm.add_transition('N', 'Y', 'open')
        self.fsm.default_start_state = 'N'
        self.fsm.initialize()
    
    def open(self):
        self.fsm.process_event('open')
        
    def close(self):
        self.fsm.process_event('close')
        
    def show(self):
        print('current_state', self.fsm.current_state)
        print('terminated', self.fsm.terminated)

       
def def_status_tt():
    ss = SwitchState()
    print(ss)
    
    ss.show()
    
    ss.open()
#     ss.open() # 不能重复open()
    print(ss)
    
    ss.close()
    print(ss)

if __name__ == '__main__':
    def_status_tt()
    