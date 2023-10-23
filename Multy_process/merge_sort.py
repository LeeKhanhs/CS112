import time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    


    return merge(left_half, right_half)

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
        arr = [float(i) for i in arr]   

    n = len(arr)

    start = time.time()
    arr_sorted = merge_sort(arr)
    end = time.time()
    print(end - start)
    # print(arr_sorted)