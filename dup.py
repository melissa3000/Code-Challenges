"""In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

For example:

dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].
dup(["kelless","keenness"]) = ["keles","kenes"].
Strings will be alphabet characters only. Don't worry about lower and upper case. See test cases for more examples.

"""


def dup(arry):
    result = []
    word = ''

    for item in arry:
        word = item[0]
        for i in range(1, len(item)):

            if item[i - 1] != item[i]:
                word += item[i]

        result.append(word)
    return result


dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]) # ==> ['codewars','picaniny','hubububo']
dup(["abracadabra","allottee","assessee"]) # ['abracadabra','alote','asese']
