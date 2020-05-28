def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    if arr == [9]:
        return [1, 0]
    elif arr[-1] < 9:
        arr[-1] += 1
    else:
        arr = add_one(arr[:-1]) + [0]
    return arr


# prints [1, 0, 0, 0]
print(add_one([9, 9, 9]))
