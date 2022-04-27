from schedulingAlgo import *
s = scheduling_algo(3)
s.add_process(1,0,5)
s.add_process(2,2,3)
s.add_process(3,4,2)
s.FCFS()
s.RR(2)
s.FCFS_Arrival()
s.best_Waiting_time(1)