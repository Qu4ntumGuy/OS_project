from RR import findavgTime

if __name__ == "__main__":
    print("Enter the number of processes: ")
    n = int(input())
    proc = []
    bt = []
    for i in range(n):
        print("Enter burst time for process ", i + 1)
        bt.append(int(input()))
        proc.append(i+1)

    print("Enter the time quantum: ")
    quantum = int(input())
findavgTime(proc, n, bt, quantum)