

def duplicate_count(text):
    """
    >>> duplicate_count("abcdeA")
    1

    >>> duplicate_count("aA11")
    2
    """

    text = text.lower()
    duplicates = 0
    letter_count = {}
    for letter in text:
        if letter_count.get(letter, 0) == 0:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    # print letter_count

    for count in letter_count.values():
        if count > 1:
            duplicates += 1
    print duplicates



# duplicate_count("abcdeA") # ==> 1
# duplicate_count("aA11") # ==> 2



