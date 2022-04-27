from RR import findavgTime
from FCFS_Arrival import avgFCFS_A_Time
from FCFS import avgFCFS_Time
from SRTF import avgSRTF_Time
from SJF import avgSJF_Time

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

   def FCFS(self):
      avgFCFS_A_Time(self.proc, self.n, self.bt, self.at)

#     print("Enter the number of processes: ")
#     n = int(input())
#     proc = []
#     bt = []
#     at = []
#     for i in range(n):
#         print("Enter burst time for process ", i + 1)
#         bt.append(int(input()))
#         proc.append(i+1)
#     print("Enter the time quantum: ")
#     quantum = int(input())

# for i in range(n):
#     print("Enter Arrival Time for ",i+1)
#     at.append(int(input()))

# print("\n-----------------For FCFS with Arrival -------------------")
# print("")
# avgFCFS_A_Time(proc, n, bt, at)

# print("\n -----------------For Round Robin-------------------")
# print("")
# findavgTime(proc, n, bt, quantum)

# print("\n -----------------For FCFS -------------------")
# print("")
# avgFCFS_Time(proc, n, bt)

# print("-----------------For SJF -------------------")
# print("")
# avgSJF_Time(n)

s = scheduling_algo(3)
s.add_process(1,0,5)
s.add_process(2,2,3)
s.add_process(3,4,2)
s.FCFS()


