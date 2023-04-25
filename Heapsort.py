def heapify(arr, n, i):
    largest = i
    # nút con bên trái
    l = 2 * i + 1
    # nút con bên phải
    r = 2 * i + 2
    # kiểm tra xem giá trị của nút con trái có lớn hơn giá trị của nút cha hay không
    # Nếu có, hàm gán largest cho chỉ số của nút có giá trị lớn nhất.
    if l < n and arr[l] > arr[largest]:
        largest = l
    # kiểm tra xem giá trị của nút con trái có lớn hơn giá trị của nút cha hay không
    # Nếu có, hàm gán largest cho chỉ số của nút có giá trị lớn nhất.
    if r < n and arr[r] > arr[largest]:
        largest = r
    # nếu largest khác với i thì hàm đổi chỗ giá trị của nút i và nút có chỉ số largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # sau đó hàm đệ quy gọi lại heapify để tiếp tục tạo heap với nút có chỉ số largest làm gốc.
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    # Xây dựng heap từ danh sách
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Lấy phần tử lớn nhất trong heap và đưa vào cuối danh sách
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

arr = [9,7,5,3,1,2,4,6,8]
print(heapsort(arr))