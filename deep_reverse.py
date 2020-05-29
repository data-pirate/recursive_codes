# Example
# Input: [1, 2, [3, 4, 5], 4, 5]
# Output: [5, 4, [5, 4, 3], 2, 1]


def deep_reverse(arr):
    """
    :params: input list
    Return - reversed list of the input list
    """
    if len(arr) <= 1:
        return arr
    output = list()
    for idx in reversed(range(0, len(arr))):
        if isinstance(arr[idx], list):
            output.append(deep_reverse(arr[idx]))
        else:
            output.append(arr[idx])
    return output


print(deep_reverse([1, 2, [3, 4, 5], 4, 5]))
