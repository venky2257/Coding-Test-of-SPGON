def reverse_string_increment_by_one(input1):
    # Strings are immutable in python. so it is not advisible to modify them
    # so we created a list with the input1 values

    # check if the string is empty
    if len(input1) == 0:
        return ('empty String')

    # storing the string in a reverse order in input_list
    input1_list = list(input1[::-1].upper())

    # iterating each char in the input_list
    for char in range(len(input1_list)):
        # ord will returns the ascii value of the char

        # if character z appears in string - as character z doesnt contain any next letter
        # we set character A as the next letter

        if ord(input1_list[char]) == 90:
            next_char = 65

        else:
            # as we needed the next character we increment the ascii value by '1'
            next_char = ord(input1_list[char]) + 1

            # modify the old character of input list with new character
        input1_list[char] = chr(next_char)

        # convert the input_list into string and strong it in input
        input1 = ''.join(input1_list)

    return str(input1)


print(reverse_string_increment_by_one('KDIOSLO'))
print(reverse_string_increment_by_one('INDIAN'))
