def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Lỗi 1: Không hoán đổi phần tử tại vị trí min_idx với phần tử tại vị trí i
        # Sửa lỗi: Thêm dòng sau để hoán đổi hai phần tử
        # arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Lỗi 2: Không kiểm tra trường hợp i và min_idx giống nhau, dẫn đến việc sắp xếp không đúng
        # Sửa lỗi: Thêm điều kiện để kiểm tra nếu i khác với min_idx thì mới hoán đổi
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Kiểm tra với danh sách đầu vào
input_list = [5, 2, 9, 1, 5, 6]
sorted_list = selection_sort(input_list)
print("Danh sách đã sắp xếp:", sorted_list)