import tkinter as tk
from RR import findavgTime
from FCFS_Arrival import avgFCFS_A_Time
from FCFS import avgFCFS_Time
from SRTF import avgSRTF_Time

win = tk.Tk()
win.geometry("400x400")
win.title("OS_Algorithm")
win.resizable(0,0)

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

def onClick():
    tk.Label(win, text="Hello World").pack()

tk.Button(win, text="Click Me", command=findavgTime(proc, n, bt, quantum)).pack()

win.mainloop()


# print("\n -----------------For Round Robin-------------------")

# findavgTime(proc, n, bt, quantum)

# print("\n -----------------For FCFS -------------------")

# avgFCFS_Time(proc, n, bt)

# print("-----------------For FCFS Arrival -------------------")

# for i in range(n):
#     print("Enter Arrival Time for ",i+1)
#     at.append(int(input()))

# avgFCFS_A_Time(proc, n, bt, at)

# print("-----------------For SRTF -------------------")

# # avgSRTF_Time(proc, n, bt)

