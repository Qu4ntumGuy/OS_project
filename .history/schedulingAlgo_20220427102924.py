from RR import findavgTime
from FCFS_Arrival import avgFCFS_A_Time
from FCFS import avgFCFS_Time
from SRTF import avgSRTF_Time
from SJF import avgSJF_Time
from prettytable import PrettyTable

if __name__ == "__main__":
    print("Enter the number of processes: ")
    n = int(input())
    proc = []
    bt = []
    at = []
    for i in range(n):
        print("Enter burst time for process ", i + 1)
        bt.append(int(input()))
        proc.append(i+1)
    print("Enter the time quantum: ")
    quantum = int(input())

print("\n-----------------For FCFS with Arrival -------------------")
print("")
avgFCFS_A_Time(proc, n, bt, at)

# print("\n -----------------For Round Robin-------------------")
# print("")
# findavgTime(proc, n, bt, quantum)

# print("\n -----------------For FCFS -------------------")
# print("")
# avgFCFS_Time(proc, n, bt)


# for i in range(n):
#     print("Enter Arrival Time for ",i+1)
#     at.append(int(input()))

# print("-----------------For SJF -------------------")
# print("")
# avgSJF_Time(n)

# print("-----------------For SRTF -------------------")

# avgSRTF_Time(proc, n, bt)
