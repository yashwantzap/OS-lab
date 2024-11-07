import multiprocessing

def increment(shared_value):
    for _ in range(100):
        shared_value.value += 1

if __name__ == "__main__":
    shared_value = multiprocessing.Value('i', 0)  # 'i' stands for integer
    processes = []

    for _ in range(5):
        p = multiprocessing.Process(target=increment, args=(shared_value,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Final value: {shared_value.value}")
