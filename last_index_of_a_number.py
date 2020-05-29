# PROBLEM STATEMENT
# Given an array arr and a target element target,
# find the last index of occurence of target in arr
# using recursion. If target is not present in arr, return -1.

# Example:
# For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 5, output = 6

# For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 7, output = -1


def last_index(arr, target):
    """
    :params: arr - input array
    :params: target - integer element
    Returns - last index of integer in arr
    """
    return last_index_solution(arr, target, len(arr) - 1)


def last_index_solution(arr, target, index):
    if index < 0:
        return -1
    if arr[index] == target:
        return index
    return last_index_solution(arr, target, index - 1)


# prints 6
print(last_index([1, 2, 5, 5, 1, 2, 5, 4], 5))
