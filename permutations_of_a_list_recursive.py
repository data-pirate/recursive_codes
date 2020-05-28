# PROBLEM STATEMENT
# Given a list of items, the goal is to find all of the
# permutations of that list. For example,
# Given a list like: [0, 1, 2]
# Permutations: [[0, 1, 2], [0, 2, 1], [1, 0, 2],
# [1, 2, 0], [2, 0, 1], [2, 1, 0]]

# we would need to use deepcopy function

import copy


def permutations(arr):
    """
    Args: myList: list of items to be permuted
    Returns: compound list: list of permutation with each
    permuted item being represented by a list
    """
    compound_list = list()
    if len(arr) == 0:
        compound_list.append([])
    else:
        first_char = arr[0]
        the_rest = slice(1, None)

        sub_list = permutations(arr[the_rest])

        for a_list in sub_list:
            for i in range(0, len(a_list) + 1):
                b_list = copy.deepcopy(a_list)
                b_list.insert(i, first_char)
                compound_list.append(b_list)
    return compound_list


# prints [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
print(sorted(permutations([0, 1, 2])))
