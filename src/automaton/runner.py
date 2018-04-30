# -*- coding: utf-8 -*-
'''
Created on 2018年4月16日

@author: Administrator
'''
from automaton import machines
from automaton import runners


def cb_on_enter(new_state, triggered_event):
    print('Enter:%s, event:%s' %(new_state, triggered_event))

def cb_on_exit(old_state, triggered_event):
    print('Exit:%s, event:%s' %(old_state, triggered_event))
    
def grow_reaction(old_state, new_state, event_trigger):
    print('grow reaction', old_state, new_state, event_trigger)
    return 'study'

def study_reaction(old_state, new_state, event_trigger):
    print('study reaction', old_state, new_state, event_trigger)
    return 'work'
 
def work_reaction(old_state, new_state, event_trigger):
    print('work reaction', old_state, new_state, event_trigger)
    return 'sick'
    
def sick_reaction(old_state, new_state, event_trigger):
    print('sick reaction', old_state, new_state, event_trigger)
    return None
        
class ManState():
    def __init__(self):
        self.fsm = machines.FiniteMachine()
        self.define_state()
        
    def __repr__(self):
        return self.fsm.pformat()
      
    def define_state(self):
        self.fsm.add_state('baby', on_enter=cb_on_enter, on_exit=cb_on_exit)
        self.fsm.add_state('youth', on_enter=cb_on_enter, on_exit=cb_on_exit)
        self.fsm.add_state('adult', on_enter=cb_on_enter, on_exit=cb_on_exit)
        self.fsm.add_state('elder', on_enter=cb_on_enter, on_exit=cb_on_exit)
        self.fsm.add_state('dead', terminal=True, on_enter=cb_on_enter, on_exit=cb_on_exit)
        
        self.fsm.default_start_state = 'baby'
        
        self.fsm.add_transition('baby', 'youth', 'grow')
        self.fsm.add_transition('youth', 'adult', 'study')
        self.fsm.add_transition('adult', 'elder', 'work')
        self.fsm.add_transition('elder', 'dead', 'sick')
        
        self.fsm.add_reaction('youth', 'grow', grow_reaction)
        self.fsm.add_reaction('adult', 'study', study_reaction)
        self.fsm.add_reaction('elder', 'work', work_reaction)
        self.fsm.add_reaction('dead', 'sick', sick_reaction)
#         self.fsm.initialize()    # run_iter中调用initialize()
    
    def show(self):
        print('current_state', self.fsm.current_state)
        print('terminated', self.fsm.terminated)

    def run(self, action):
        self.runner = runners.FiniteRunner(self.fsm)
        for (old, new) in self.runner.run_iter(action):
            print(old, '-->', new)
            self.show()
        
        
def runner_tt():
    ss = ManState()
    print(ss)
    ss.run('grow')

if __name__ == '__main__':
    runner_tt()
    