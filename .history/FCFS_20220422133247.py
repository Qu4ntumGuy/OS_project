# Python3 program for implementation
# of FCFS scheduling

# Function to find the waiting
# time for all processes
def findWaitingTime(processes, n,
					bt, wt):

	# waiting time for
	# first process is 0
	wt[0] = 0

	# calculating waiting time
	for i in range(1, n ):
		wt[i] = bt[i - 1] + wt[i - 1]

# Function to calculate turn
# around time
def findTurnAroundTime(processes, n,
					bt, wt, tat):

	# calculating turnaround
	# time by adding bt[i] + wt[i]
	for i in range(n):
		tat[i] = bt[i] + wt[i]

# Function to calculate
# average time
def findavgTime( processes, n, bt):

	wt = [0] * n
	tat = [0] * n
	total_wt = 0
	total_tat = 0

	# Function to find waiting
	# time of all processes
	findWaitingTime(processes, n, bt, wt)

	# Function to find turn around
	# time for all processes
	findTurnAroundTime(processes, n,
					bt, wt, tat)

	# Display processes along
	# with all details
	print( "Processes Burst time " +
				" Waiting time " +
				" Turn around time")

	# Calculate total waiting time
	# and total turn around time
	for i in range(n):
	
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" " + str(i + 1) + "\t\t" +
					str(bt[i]) + "\t " +
					str(wt[i]) + "\t\t " +
					str(tat[i]))

	print( "Average waiting time = "+
				str(total_wt / n))
	print("Average turn around time = "+
					str(total_tat / n))

# Driver code
if __name__ =="__main__":
	
	# process id's
	processes = [ 1, 2, 3]
	n = len(processes)

	# Burst time of all processes
	burst_time = [10, 5, 8]

	findavgTime(processes, n, burst_time)

# This code is contributed
# by ChitraNayal








# Python3 program for implementation of FCFS  
# scheduling with different arrival time  
  
# Function to find the waiting time 
# for all processes  
def findWaitingTime(processes, n, bt, wt, at):  
    service_time = [0] * n  
    service_time[0] = 0
    wt[0] = 0
  
    # calculating waiting time  
    for i in range(1, n):  
          
        # Add burst time of previous processes  
        service_time[i] = (service_time[i - 1] +
                                     bt[i - 1])  
  
        # Find waiting time for current 
        # process = sum - at[i]  
        wt[i] = service_time[i] - at[i]  
  
        # If waiting time for a process is in  
        # negative that means it is already  
        # in the ready queue before CPU becomes  
        # idle so its waiting time is 0  
        if (wt[i] < 0): 
            wt[i] = 0
      
# Function to calculate turn around time  
def findTurnAroundTime(processes, n, bt, wt, tat):  
      
    # Calculating turnaround time by 
    # adding bt[i] + wt[i]  
    for i in range(n): 
        tat[i] = bt[i] + wt[i]  
  
  
# Function to calculate average waiting  
# and turn-around times.  
def findavgTime(processes, n, bt, at):  
    wt = [0] * n 
    tat = [0] * n  
  
    # Function to find waiting time 
    # of all processes  
    findWaitingTime(processes, n, bt, wt, at)  
  
    # Function to find turn around time for 
    # all processes  
    findTurnAroundTime(processes, n, bt, wt, tat)  
  
    # Display processes along with all details  
    print("Processes   Burst Time   Arrival Time     Waiting",  
          "Time   Turn-Around Time  Completion Time
") 
    total_wt = 0
    total_tat = 0
    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        compl_time = tat[i] + at[i]  
        print(" ", i + 1, " ", bt[i], " ", at[i],  
              " ", wt[i], " ", tat[i], " ", compl_time)  
  
    print("Average waiting time = %.5f "%(total_wt /n)) 
    print("
Average turn around time = ", total_tat / n)  
  
# Driver code  
if __name__ =="__main__": 
      
    # Process id's  
    processes = [1, 2, 3] 
    n = 3
  
    # Burst time of all processes  
    burst_time = [5, 9, 6]  
  
    # Arrival time of all processes  
    arrival_time = [0, 3, 6]  
  
    findavgTime(processes, n, burst_time, 
                            arrival_time) 
  
# This code is contributed 
# Shubham Singh(SHUBHAMSINGH10