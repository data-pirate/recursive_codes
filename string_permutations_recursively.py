def string_permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    """
    return solution(string, 0)


def solution(string, index):
    compoundList = list()

    if index >= len(string):
        return [""]
    else:
        sub_string = solution(string, index + 1)

        current_char = string[index]

        for a_string in sub_string:
            for i in range(0, len(a_string) + 1):
                b_string = a_string[:i] + current_char + a_string[i:]
                compoundList.append(b_string)
    return compoundList


print(string_permutations('abc'))
