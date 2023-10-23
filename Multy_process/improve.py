import multiprocessing
import time

def merge_sort_worker(arr, result_queue):
    result_queue.put(sorted(arr))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

if __name__ == "__main__":
    with open("array.txt", "r") as file:
        arr = file.readline().strip().split(" ")
        arr = [int(i) for i in arr]

    num_processes = multiprocessing.cpu_count()
    chunk_size = len(arr) // num_processes

    processes = []
    result_queue = multiprocessing.Queue()

    for i in range(num_processes):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size if i < num_processes - 1 else len(arr)
        process = multiprocessing.Process(target=merge_sort_worker, args=(arr[start_idx:end_idx], result_queue))
        processes.append(process)

    start = time.time()

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    sorted_chunks = [result_queue.get() for _ in range(num_processes)]

    while len(sorted_chunks) > 1:
        merged_chunks = []
        for i in range(0, len(sorted_chunks), 2):
            if i + 1 < len(sorted_chunks):
                merged = merge(sorted_chunks[i], sorted_chunks[i + 1])
            else:
                merged = sorted_chunks[i]
            merged_chunks.append(merged)
        sorted_chunks = merged_chunks

    end = time.time()

    print(sorted_chunks[0])
    print((end - start), " ms")
