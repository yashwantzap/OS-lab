def first_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)  # -1 indicates no allocation
    
    for i in range(len(processes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= processes[i]:
                allocation[i] = j  # Allocate this block
                memory_blocks[j] -= processes[i]  # Reduce the block size
                break

    return allocation


def best_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)  # -1 indicates no allocation
    
    for i in range(len(processes)):
        best_idx = -1
        min_diff = float('inf')
        
        # Find the best fit block for the process
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= processes[i] and memory_blocks[j] - processes[i] < min_diff:
                best_idx = j
                min_diff = memory_blocks[j] - processes[i]

        if best_idx != -1:
            allocation[i] = best_idx
            memory_blocks[best_idx] -= processes[i]  # Reduce the block size

    return allocation


def worst_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)  # -1 indicates no allocation
    
    for i in range(len(processes)):
        worst_idx = -1
        max_diff = -float('inf')
        
        # Find the worst fit block for the process
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= processes[i] and memory_blocks[j] - processes[i] > max_diff:
                worst_idx = j
                max_diff = memory_blocks[j] - processes[i]

        if worst_idx != -1:
            allocation[i] = worst_idx
            memory_blocks[worst_idx] -= processes[i]  # Reduce the block size

    return allocation


def display_allocation(allocation, method):
    print(f"\nMemory Allocation using {method}:")
    print(f"Process\tSize\tBlock")
    
    for i in range(len(allocation)):
        if allocation[i] != -1:
            print(f"{i+1}\t{processes[i]}\t{allocation[i]+1}")  # +1 for human-readable indexing
        else:
            print(f"{i+1}\t{processes[i]}\tNot Allocated")


# Input and main logic
def main():
    # User input for number of memory blocks and processes
    n_blocks = int(input("Enter the number of memory blocks: "))
    n_processes = int(input("Enter the number of processes: "))

    memory_blocks = []
    processes = []

    # Input memory block sizes
    print(f"Enter the sizes of {n_blocks} memory blocks:")
    for i in range(n_blocks):
        memory_blocks.append(int(input(f"Size of memory block {i+1}: ")))

    # Input process sizes
    print(f"Enter the sizes of {n_processes} processes:")
    for i in range(n_processes):
        processes.append(int(input(f"Size of process {i+1}: ")))

    # Ask user for the allocation method
    print("\nChoose the memory allocation method:")
    print("1. First Fit")
    print("2. Best Fit")
    print("3. Worst Fit")
    choice = int(input("Enter your choice (1/2/3): "))

    # Call appropriate allocation function
    if choice == 1:
        allocation = first_fit(memory_blocks.copy(), processes)
        display_allocation(allocation, "First Fit")
    elif choice == 2:
        allocation = best_fit(memory_blocks.copy(), processes)
        display_allocation(allocation, "Best Fit")
    elif choice == 3:
        allocation = worst_fit(memory_blocks.copy(), processes)
        display_allocation(allocation, "Worst Fit")
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

Enter the number of memory blocks: 5
Enter the number of processes: 4
Enter the sizes of 5 memory blocks:
Size of memory block 1: 200
Size of memory block 2: 500
Size of memory block 3: 300
Size of memory block 4: 100
Size of memory block 5: 600
Enter the sizes of 4 processes:
Size of process 1: 212
Size of process 2: 417
Size of process 3: 112
Size of process 4: 426
Choose the memory allocation method:
1. First Fit
2. Best Fit
3. Worst Fit
Enter your choice (1/2/3): 2
