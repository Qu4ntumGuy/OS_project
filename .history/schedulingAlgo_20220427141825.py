from RR import *
from FCFS_Arrival import *
from FCFS import *
from SRTF import *
from SJF import *

class scheduling_algo:
   def __init__(self,n):
      self.n=n
      self.at= []
      self.bt= []
      self.proc= []

   def add_process(self,index,at,bt):
      self.proc.append(index)
      self.at.append(at)
      self.bt.append(bt)

# ------------------------FCFS----------------------------- 

   def FCFS(self):
      avgFCFS_Time(self.proc, self.n, self.bt)

   def FCFS_waiting_time(self):
      ans = avgFCFS_Time_waiting(self.proc, self.n, self.bt)
      return ans

   def FCFS_turnRound_time(self):
      ans = avgFCFS_Time_turnRound(self.proc, self.n, self.bt)
      return ans

#----------------------FCFS With Arrival---------------------

   def FCFS_Arrival(self):
      avgFCFS_A_Time(self.proc, self.n, self.bt, self.at)

   def FCFS_A_waiting_time(self):
       ans = avgFCFS_A_Time_waiting(self.proc, self.n, self.bt, self.at)
       return ans 

   def FCFS_A_turnRound_time(self):
      ans = avgFCFS_A_Time_turnRound(self.proc, self.n, self.bt, self.at)
      return ans

#----------------------Round Robin-----------------------------

   def RR(self,quantum):
      findavgTime(self.proc, self.n, self.bt, quantum)

   def RR_waiting_time(self,quantum):
      ans = avgRR_Time_waiting(self.proc, self.n, self.bt, quantum)
      return ans

   def RR_turnRound_time(self,quantum):
      ans = avgRR_Time_turnRound(self.proc, self.n, self.bt, quantum)
      return ans
