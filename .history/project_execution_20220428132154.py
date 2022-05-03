from schedulingAlgo import *
s = scheduling_algo(3)
s.add_process(1,0,2)
s.add_process(2,2,3)
s.add_process(3,3,4)
ans1 = s.best_TurnRound_time(2)
print(ans1)