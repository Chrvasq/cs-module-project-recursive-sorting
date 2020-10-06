# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    left = 0
    right = 0
    merged_arr = []

    while left < len(arrA) and right < len(arrB):
        if arrA[left] <= arrB[right]:
            merged_arr.append(arrA[left])
            left += 1
        else:
            merged_arr.append(arrB[right])
            right += 1
    while left < len(arrA):
        merged_arr.append(arrA[left])
        left += 1
    while right < len(arrB):
        merged_arr.append(arrB[right])
        right += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    return merge(merge_sort(left), merge_sort(right))


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
