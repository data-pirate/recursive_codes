# PROBLEM STATEMENT
# arr = [9, 12, 15]
# output =  [[],
#            [15],
#            [12],
#            [12, 15],
#            [9],
#            [9, 15],
#            [9, 12],
#            [9, 12, 15]]


def subsets(arr):
    """
    :params: input list
    Returns - a list of all subsets of the list
    """
    return subsets_solver(arr, 0)


def subsets_solver(arr, index):
    if index >= len(arr):
        return [[]]

    output = list()
    small_output = subsets_solver(arr, index + 1)

    for element in small_output:
        output.append(element)

    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return sorted(output)


print(subsets([9, 12, 15]))
