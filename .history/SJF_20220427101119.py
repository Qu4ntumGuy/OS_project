def arrangeArrival(n, array):
    for i in range(0, n):
        for j in range(i, n-i-1):
            if array[1][j] > array[1][j+1]:
                for k in range(0, n):
                    array[k][j], array[k][j+1] = array[k][j+1], array[k][j]

def CompletionTime(n, array):
    value = 0
    array[3][0] = array[1][0] + array[2][0]
    array[5][0] = array[3][0] - array[1][0]
    array[4][0] = array[5][0] - array[2][0]
    for i in range(1, n):
        temp = array[3][i-1]
        mini = array[2][i]
        for j in range(i, n):
            if temp >= array[1][j] and mini >= array[2][j]:
                mini = array[2][j]
                value = j
        array[3][value] = temp + array[2][value]
        array[5][value] = array[3][value] - array[1][value]
        array[4][value] = array[5][value] - array[2][value]
        for k in range(0, 6):
            array[k][value], array[k][i] = array[k][i], array[k][value]

def avgSJF_Time(process, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    for i in range(0, n):
        wt[i] = bt[i]
    for i in range(1, n):
        for j in range(0, n):
            if wt[j] > wt[j+1]:
                wt[j], wt[j+1] = wt[j+1], wt[j]
                for k in range(0, n):
                    process[k][j], process[k][j+1] = process[k][j+1], process[k][j]
    for i in range(0, n):
        tat[i] = wt[i] + bt[i]
    for i in range(0, n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
    print("Processes Burst time " + " Waiting time " + " Turn around time")
    for i in range(0, n):
        print(" " + str(i + 1) + "\t\t" + str(bt[i]) + "\t " + str(wt[i]) + "\t\t " + str(tat[i]))
    print("Average waiting time = "+ str(total_wt / n))
    print("Average turn around time = "+ str(total_tat / n))
    


# if __name__ == '__main__':
#     n = 4
#     arr = [[int(i) for i in range(1, n+1)], [2, 0, 4, 5],
#            [3, 4, 2, 4], [0]*n, [0]*n, [0]*n]
#     arrangeArrival(n, arr)
#     CompletionTime(n, arr)
#     print("Process \tArrival \tBurst \t    Completion \t      Waiting \t    Turnaround ")
#     waitingtime = 0
#     turaroundtime = 0
#     for i in range(0, n):
#         print(arr[0][i], "\t\t", arr[1][i], "\t\t", arr[2][i],
#               "\t\t", arr[3][i], "\t\t", arr[4][i], "\t\t", arr[5][i])
#         waitingtime += arr[4][i]
#         turaroundtime += arr[5][i]
#     print("Average waiting time is ", (waitingtime/n))
#     print("Average Turnaround Time is ", (turaroundtime/n))
