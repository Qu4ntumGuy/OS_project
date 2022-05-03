from schedulingAlgo import *
s = scheduling_algo(3)
s.add_process(1,0,3)
s.add_process(2,2,3)
s.add_process(3,3,3)
s.FCFS()