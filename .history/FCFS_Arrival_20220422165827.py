def findWaitingTime(processes, n, bt, wt, at):
    service_time = [0] * n
    service_time[0] = 0
    wt[0] = 0

    for i in range(1, n):
        service_time[i] = (service_time[i - 1] + bt[i - 1])

        wt[i] = service_time[i] - at[i]
        if (wt[i] < 0):
            wt[i] = 0

def findTurnAroundTime(processes, n, bt, wt, tat):
    # adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, bt, at):
    wt = [0] * n
    tat = [0] * n

    findWaitingTime(processes, n, bt, wt, at)
    findTurnAroundTime(processes, n, bt, wt, tat)
    print("Processes   Burst Time   Arrival Time     Waiting","Time   Turn-Around Time  Completion Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time = tat[i] + at[i]
        print("   ", i + 1, "\t", bt[i], "\t", at[i],"\t", wt[i], "\t", tat[i], "\t", compl_time)
    print("Average waiting time = %.5f " % (total_wt / n))
    print("Average turn around time = ", total_tat / n)


# Driver code
if __name__ == "__main__":

    # Process id's
    processes = [1, 2, 3]
    n = 3

    # Burst time of all processes
    burst_time = [5, 9, 6]

    # Arrival time of all processes
    arrival_time = [0, 3, 6]

    findavgTime(processes, n, burst_time, arrival_time)
