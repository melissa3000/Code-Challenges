"""Given a number, return a string with dash'-'marks before and after each
odd integer, but do not begin or end the string with a dash mark.
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
"""


def dashatize(num):
    """
    >>> dashatize(274)
    '2-7-4'

    >>> dashatize(6815)
    '68-1-5'

    >>> dashatize(5311)
    '5-3-1-1'
    """

    # result = ''
    # num_str = str(num)
    # for number in num_str:
    #     if int(number) % 2 == 0:
    #         result += number
    #     else:
    #         result += "-" + number + "-"

    # if result[0] == "-":
    #     result = result[1:]

    # if result[-1] == "-":
    #     result = result[:-1]



    # print result

    if num == None:
        return None

    if num < 0:
        num = -num

    result = ''
    num_str = str(num)

    for i in range(len(num_str)):
        if int(num_str[i]) % 2 == 0:
            result += num_str[i]

        # if number is odd and the number before is even
        if int(num_str[i]) % 2 != 0 and int(num_str[i - 1])  % 2 == 0:
            result += "-" + num_str[i] + "-"

        # if number is odd and the number before is odd
        if int(num_str[i]) % 2 != 0 and int(num_str[i - 1])  % 2 != 0:
            result += num_str[i] + "-"


    if result[-1] == "-":
        result = result[:-1]
    if result[0] == "-":
        result = result[1:]

    return result




# dashatize(274) #-> '2-7-4'
# dashatize(6815) #-> '68-1-5'
# dashatize(5311) #==> '5-3-1-1'
dashatize(974302)

