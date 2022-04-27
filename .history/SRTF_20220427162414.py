from concurrent.futures import process
from prettytable import PrettyTable


def findWaitingTime(processes, n):
    rt = [0] * n
    for i in range(n):
        rt[i] = processes[i][1]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False
    while (complete != n):
        for j in range(n):
            if ((processes[j][2] <= t) and
                    (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
        if (check == False):
            t += 1
            continue

        rt[short] -= 1
        minm = rt[short]
        if (minm == 0):
            minm = 999999999

        if (rt[short] == 0):
            complete += 1
            check = False
            fint = t + 1
            wt[short] = (fint - processes[short][1] - processes[short][2])
            if (wt[short] < 0):
                wt[short] = 0
        t += 1


def findTurnAroundTime(processes, n, wt, tat):
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]


def avgSRTF_Time(processes, n):
    wt = [0] * n
    tat = [0] * n
    findWaitingTime(processes, n, wt)
    findTurnAroundTime(processes, n, wt, tat)
    table = PrettyTable(
        ["Processes", "Burst Time", "Waiting Time", "Turn-Around Time"])
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print([processes[i][0], processes[i][1], wt[i], tat[i]])

    print("\nAverage waiting time = %.5f " % (total_wt / n))
    print("Average turn around time = ", total_tat / n)


def avgSRTF_Time_waiting(processes, n):
    wt = [0] * n
    tat = [0] * n
    findWaitingTime(processes, n, wt)
    findTurnAroundTime(processes, n, wt, tat)
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    return total_wt / n
