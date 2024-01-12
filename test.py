def quicksort(arr, low, high):
    if low < high:
        # Partition the array into two sub-arrays
        pivot_index = partition(arr, low, high)

        # Recursively sort the sub-arrays
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]

    # Initialize the index of the smaller element
    i = low - 1

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        print(i, j)
        if arr[j] <= pivot:
            # Swap arr[i] and arr[j]
            i = i + 1
            print('arr before swap', arr)
            print(f'swap {arr[i]} and {arr[j]} in pos {i}, {j}')
            arr[i], arr[j] = arr[j], arr[i]
            print('arr after swap', arr)

    # Swap arr[i+1] and arr[high] to place the pivot element at its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f'SWAP ARRAY arr[i + 1] : {arr[i + 1]}  with arr[high] : {arr[high]}')
    
    return i + 1

# Example usage:
arr = [1, 5, 3, 2, 6, 8, 10, 2, 4]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
