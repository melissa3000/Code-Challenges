"""
A string is considered to be in title case if each word in the string is either
(a) capitalised (that is, only the first letter of the word is in upper case) or
(b) considered to be an exception and put entirely into lower case unless it is
the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional
list of exceptions (minor words). The list of minor words will be given as a
string with each word separated by a space. Your function should ignore the case
of the minor words string -- it should behave in the same way even if the case
of the minor word string is changed."""


def title_case(title, minor_words = ''):

    result = ''

    if len(title) == 0:
        print result

    title_lst = title.lower().split(" ")
    minor_words = minor_words.lower().split(" ")

    first_word = title_lst[0][0].upper() + title_lst[0][1:]

    if len(title_lst) == 1:
        return first_word

    for i in range(1, len(title_lst)):
        if title_lst[i] not in minor_words:
            word = title_lst[i][0].upper() + title_lst[i][1:]
        else:
            word = title_lst[i].lower()
        result += word + " "
    print first_word + " " + result[0:-1]


# title_case('') #==> ''
title_case('a clash of KINGS', 'a an the of') #==> 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') #==> 'The Wind in the Willows'
title_case('the quick brown fox') #==> 'The Quick Brown Fox'
