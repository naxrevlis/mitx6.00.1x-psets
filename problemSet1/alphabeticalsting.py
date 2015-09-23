import string

def get_id_in_string(i_string, i_char):
    endi = len(i_string)
    i = 0
    while i < endi:
        if i_char == i_string[i]:
            break
        i += 1
    return i


def find_longest_squence(s_string):
    longest_string = ''
    for i in s_string:
        if longest_string == '':
            n_start = 0
        else:
            n_start = get_id_in_string(
                string.ascii_lowercase, longest_string[-1])
        if i in string.ascii_lowercase[n_start:]:
            longest_string += i
        else:
            break
        print 'Find longes sequence: ', longest_string
    return longest_string


alphabeticalstring = string.ascii_lowercase
longest_string_temp = ''
longest_string = ''
add_char_i = 0
s = 'hpvdlsmvjrvjjjvc'
i = 0
while i < len(s):
    id_in_s = get_id_in_string(s, s[i])
    longest_string_temp = find_longest_squence(s[i:])
    print s[id_in_s:]
    if (len(longest_string_temp) > len(longest_string)):
        longest_string = longest_string_temp
    longest_string_temp = ''
    i += 1
print "Longest substring in alphabetical order is: ", longest_string
