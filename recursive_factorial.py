def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

# returns 24
print(factorial(4))
