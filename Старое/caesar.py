def shift_encode(string_to_encode):

    result = []

    for char in string_to_encode:
        if char.isupper():
            start_alpha = 'A'
        else:
            start_alpha = 'a'

        char_index = ord(char) - ord(start_alpha)
        new_syn_index = (char_index + 1) % 26 + ord(start_alpha)
        result.append(chr(new_syn_index))

    return ' '.join(result)


#print(shift_encode('ABC'))
#print(shift_encode('abc'))
#print(shift_encode('XYZ'))


def shift_decode(string_to_encode):
    result = []

    for char in string_to_encode:
        if char.isupper():
            start_alpha = 'A'
        else:
            start_alpha = 'a'

        char_index = ord(char) - ord(start_alpha)
        new_syn_index = (char_index - 1) % 26 + ord(start_alpha)
        result.append(chr(new_syn_index))

    return ' '.join(result)


print(shift_decode('BCD'))
print(shift_decode('bcd'))
print(shift_decode('YZA'))