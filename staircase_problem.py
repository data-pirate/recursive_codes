# PROBLEM STATEMENT
# Example:
# n == 1 then answer = 1

# n == 3 then answer = 4
# The output is 4 because there are four ways we can climb the staircase:
# 1 step + 1 step + 1 step
# 1 step + 2 steps
# 2 steps + 1 step
# 3 steps

# n == 5 then answer = 13


def staircase(num):
    """
    :params: number of steps in the staircase
    Returns - number of possible ways in which you can climb the staircase
    """
    if num <= 0:
        return 1
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    return staircase(num - 1) + staircase(num - 2) + staircase(num - 3)


# prints 13
print(staircase(5))
