ii# Scheduling Algorithms in Python
def fcfs(processes, n):
    # Sorting by arrival time
    processes.sort(key=lambda x: x[1])

    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    
    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = processes[i-1][2] + waiting_time[i-1] - processes[i][1]
    
    for i in range(n):
        turnaround_time[i] = processes[i][2] + waiting_time[i]
        completion_time[i] = waiting_time[i] + processes[i][2]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time, completion_time


def sjf(processes, n):
    # Sorting by burst time
    processes.sort(key=lambda x: x[2])

    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    
    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = processes[i-1][2] + waiting_time[i-1] - processes[i][1]
    
    for i in range(n):
        turnaround_time[i] = processes[i][2] + waiting_time[i]
        completion_time[i] = waiting_time[i] + processes[i][2]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time, completion_time


def rr(processes, n, quantum):
    remaining_burst_time = [process[2] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n

    queue = []
    time = 0
    completed = 0

    while completed < n:
        for i in range(n):
            if remaining_burst_time[i] > 0 and processes[i][1] <= time:
                queue.append(i)

        if len(queue) > 0:
            idx = queue.pop(0)
            if remaining_burst_time[idx] > quantum:
                time += quantum
                remaining_burst_time[idx] -= quantum
            else:
                time += remaining_burst_time[idx]
                waiting_time[idx] = time - processes[idx][2] - processes[idx][1]
                remaining_burst_time[idx] = 0
                completed += 1
        else:
            time += 1
    
    for i in range(n):
        turnaround_time[i] = processes[i][2] + waiting_time[i]
        completion_time[i] = waiting_time[i] + processes[i][2]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time, completion_time


# Read input from a file
def read_input_file(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        processes = []
        for i in range(n):
            arrival_time, burst_time = map(int, file.readline().strip().split())
            processes.append([i, arrival_time, burst_time])  # Process id, Arrival time, Burst time
    return processes, n


# Main function to select scheduling algorithm
def main():
    file_name = input("Enter the input file name: ")
    processes, n = read_input_file(file_name)

    print("Choose the scheduling algorithm:")
    print("1. FCFS (First Come First Serve)")
    print("2. SJF (Shortest Job First)")
    print("3. RR (Round Robin)")

    choice = int(input())

    if choice == 1:
        avg_waiting_time, avg_turnaround_time, completion_time = fcfs(processes, n)
        print(f"Average Waiting Time: {avg_waiting_time}")
        print(f"Average Turnaround Time: {avg_turnaround_time}")
        print(f"Completion Times: {completion_time}")

    elif choice == 2:
        avg_waiting_time, avg_turnaround_time, completion_time = sjf(processes, n)
        print(f"Average Waiting Time: {avg_waiting_time}")
        print(f"Average Turnaround Time: {avg_turnaround_time}")
        print(f"Completion Times: {completion_time}")

    elif choice == 3:
        quantum = int(input("Enter time quantum for Round Robin: "))
        avg_waiting_time, avg_turnaround_time, completion_time = rr(processes, n, quantum)
        print(f"Average Waiting Time: {avg_waiting_time}")
        print(f"Average Turnaround Time: {avg_turnaround_time}")
        print(f"Completion Times: {completion_time}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()



!/bin/bash
read -p "Enter degree celsius temperature: " C
F=$(1.8*{$C})+32
echo The temperature in Fahrenheit is $F
in above shell script i am trying to convert
