Class Name : SchedulingAlgo

Differnt Method

s.add_process(index,arrival_time,burst_time)

###   Print Table   ###
s.FCFS()
-->Print solution table of FCFS
-->Print average waiting time
-->Print average turn around time

s.FCFS_Arrival()
-->Print solution table of FCFS with arrival time
-->Print average waiting time
-->Print average turn around time

s.SJF()
-->Print solution table of SJF
-->Print average waiting time
-->Print average turn around time

s.RR(Quantum_number)
-->Print solution table of RR
-->Need to send one argument
-->Print average waiting time
-->Print average turn around time

s.showAllTable(self,quantum)
-->Print solution table of Algo
-->Need to send one argument


###  Find Waiting Time   ###   
s.FCFS_waiting_time()
s.RR_waiting_time()
s.SJF_waiting_time()
s.FCFS_A_waiting_time()
--> It return answer


### Find Turn Around Time   ###
s.FCFS_turnRound_time()
s.FCFS_A_turnRound_time()
s.RR_turnRound_time()
s.SJF_turnRound_time()
--> It return answer

## Find Best Waiting Time  ###
s.best_Waiting_time()


## Find Best Turn Around Time  ###
s.best_TurnRound_time()
