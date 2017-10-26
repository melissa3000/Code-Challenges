"""The goal of this exercise is to convert a string to a new string where each
character in the new string is '(' if that character appears only once in the
original string, or ')' if that character appears more than once in the original
string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("

"""

from collections import Counter

def duplicate_encode(word):

    word = word.lower()

    result = ''

    d = Counter(word)

    for letter in word:
        if d.get(letter, 0) > 1:
            result += ")"
        else:
            result += "("

    print result





duplicate_encode("din") # ==> "((("
duplicate_encode("recede") # ==>  "()()()"
duplicate_encode("Success") # ==> ")())())"
duplicate_encode("(( @")  # ==>  "))(("