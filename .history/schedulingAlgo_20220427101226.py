from RR import findavgTime
from FCFS_Arrival import avgFCFS_A_Time
from FCFS import avgFCFS_Time
from SRTF import avgSRTF_Time
from SJF import avgSJF_Time

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

# win = tk.Tk()
# win.title("OS_Algorithm")

# tk.Button(win, text="Click Me", command=findavgTime(proc, n, bt, quantum)).pack()

# win.mainloop()

print("\n -----------------For Round Robin-------------------")
print("")
findavgTime(proc, n, bt, quantum)

print("\n -----------------For FCFS -------------------")
print("")
avgFCFS_Time(proc, n, bt)

print("\n-----------------For FCFS with Arrival -------------------")
print("")
for i in range(n):
    print("Enter Arrival Time for ",i+1)
    at.append(int(input()))

avgFCFS_A_Time(proc, n, bt, at)

# print("-----------------For SRTF -------------------")

# # avgSRTF_Time(proc, n, bt)

print("-----------------For SJF -------------------")

avgSJF_Time(proc, n, bt)