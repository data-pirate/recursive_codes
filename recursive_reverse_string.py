def reverse_string(string):
    if len(string) == 0:
        return ""
    else:
        first_char = string[0]
        the_rest = slice(1, None)
        reverse_sub_string = reverse_string(string[the_rest])

        return reverse_sub_string + first_char


# prints 'gnirts esrever'
print(reverse_string('reverse string'))
