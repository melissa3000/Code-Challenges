
import re

def increment_string(strng):
    strng_list = list(strng)
    last_letter = strng_list[-1]
    result = ''

    # last = re.match(r"\d+", strng)




    if last_letter in "1234567890":
        last_letter = int(last_letter) + 1
        strng_list[-1] = str(last_letter)
        result = ''.join(strng_list)
    else:
        result = strng + '1'

    return result




increment_string('foo')
increment_string("foobar001")


