# heap implementation

# Max Heapify
def max_heapify(Arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # largest so far is compared with left child
    if left < n and Arr[largest] < Arr[left]:
        largest = left

    # largest so far is compared with right child
    if right < n and Arr[largest] < Arr[right]:
        largest = right

    # change parent
    if largest != i:
        Arr[i], Arr[largest] = Arr[largest], Arr[i]
        # recursive call
        max_heapify(Arr, n, largest)


# Driver Code
Arr = [2, 66, 30, 5, 9, 10]
print("Og Array is")
print(Arr)
n = len(Arr)

# Build a max heap
for i in range(n // 2 - 1, -1, -1):
    max_heapify(Arr, n, i)

# Display
print("Max heap is")
print(Arr)