"""Create a function that transforms any positive number to a string representing
the number in words. The function should work for all numbers between 0 and 999999.

ex:
number2words(0)  ==>  "zero"
number2words(1)  ==>  "one"
"""



def number2words(n):
    """ works for numbers between 0 and 999999 """

    numstr = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
              7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
              13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
              18: 'eighteen', 19: 'nineteen', 20: 'twenty'}
    tens = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

    num_lst = [int(d) for d in str(n)]

    result = ''

    if n == 0:
        result = 'zero'



    if len(num_lst) == 6:
        result = numstr.get(num_lst[0], 0) + " hundred " + tens.get(num_lst[1], 0) + " " + numstr.get(num_lst[2], 0) + " thousand " + numstr.get(num_lst[3], 0) + " hundred " + tens.get(num_lst[4], 0) + "-" + numstr.get(num_lst[5], 0)

    elif len(num_lst) == 5:
        result = tens.get(num_lst[0], 0) + " " + numstr.get(num_lst[1], 0) + " thousand " + numstr.get(num_lst[2], 0) + " hundred " + tens.get(num_lst[3], 0) + "-" + numstr.get(num_lst[4], 0)

    elif len(num_lst) == 4:
        result = numstr.get(num_lst[0], 0) + " thousand " + numstr.get(num_lst[1], 0) + " hundred " + tens.get(num_lst[2], 0) + "-" + numstr.get(num_lst[3], 0)

    elif len(num_lst) == 3 and num_lst[1] == 0:
        result = numstr.get(num_lst[0], 0) + " hundred " + numstr.get(num_lst[2], 0)

    elif len(num_lst) == 3:
        result = numstr.get(num_lst[0], 0) + " hundred " + tens.get(num_lst[1], 0) + "-" + numstr.get(num_lst[2], 0)

    elif len(num_lst) == 2 and n > 20 and num_lst[1] == 0:
        result = tens.get(num_lst[0], 0)

    elif len(num_lst) == 2 and n > 20 and num_lst[1] != 0:
        result = tens.get(num_lst[0], 0) + "-" + numstr.get(num_lst[1], 0)

    else:
        result = numstr.get(n, 0)

    print result



number2words(0) # "zero"
number2words(1) # "one"
number2words(8) # "eight"
number2words(10) # "ten"
number2words(19) # "nineteen"
number2words(20) #"twenty"
number2words(22) # "twenty-two"
number2words(80)
number2words(999999)
number2words(103)
number2words(100)
# number2words(1003)



