def palindrome(string):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    if len(string) <= 1:
        return True
    else:
        first_char = string[0]
        last_char = string[-1]

        sub_string = string[1:-1]

        return (last_char == first_char) and palindrome(sub_string)


# prints True
print(palindrome('madam'))
