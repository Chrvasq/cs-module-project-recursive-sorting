# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    start = start
    end = end

    while start <= end:
        middle = (start + end) // 2
        guess = arr[middle]

        if guess is target:
            return middle
        elif guess > target:
            return binary_search(arr, target, start, middle - 1)
        else:
            return binary_search(arr, target, middle + 1, end)
    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target, start=0, end=None):
    start = start
    end = len(arr) - 1 if end is None else end
    first_value = arr[0]
    last_value = arr[-1]

    middle = (start + end) // 2
    guess = arr[middle]

    while start <= end:
        middle = (start + end) // 2
        guess = arr[middle]

        if guess is target:
            return middle
        elif first_value < last_value:
            if guess > target:
                return agnostic_binary_search(arr, target, start, middle - 1)
            else:
                return agnostic_binary_search(arr, target, middle + 1, end)
        else:
            if guess < target:
                return agnostic_binary_search(arr, target, start, middle - 1)
            else:
                return agnostic_binary_search(arr, target, middle + 1, end)
    return -1