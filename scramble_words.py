# Background
# There is a message that is circulating via public media that claims a reader can easily read a message where the inner letters of each words is scrambled, as long as the first and last letters remain the same and the word contains all the letters.

# Another example shows that it is quite difficult to read the text where all the letters are reversed rather than scrambled.

# In this kata we will make a generator that generates text in a similar pattern, but instead of scrambled or reversed, ours will be sorted alphabetically

# Requirement
# return a string where:
# 1) the first and last characters remain in original place for each word
# 2) characters between the first and last characters must be sorted alphabetically
# 3) punctuation should remain at the same place as it started, for example: shan't -> sahn't

# Assumptions
# 1) words are seperated by single spaces
# 2) only spaces separate words, special characters do not, for example: tik-tak -> tai-ktk
# 3) special characters do not take the position of the non special characters, for example: -dcba -> -dbca
# 4) for this kata puctuation is limited to 4 characters: hyphen(-), apostrophe('), comma(,) and period(.)
# 5) ignore capitalisation

def scramble_words(words):

    if len(words) <= 3:
        return words

    new_words = []
    result = ''

    punctuation = set(".-'?!,")
    word_lst = words.split()
    for word in word_lst:
        for letter in word:
            if letter not in punctuation:
                scramble_word =  word[0] + ''.join(sorted(word[1:-1])) + word[-1]

        for index, char in enumerate(word):
            if char in punctuation:
                removed = word.replace(char, "")
                scramble_word =  removed[0] + ''.join(sorted(removed[1:-1])) + removed[-1]
                scramble_word = scramble_word[:index] + char + scramble_word[index:]

        new_words.append(scramble_word)

    result = ' '.join(new_words)

    return result




# scramble_words('professionals') # 'paefilnoorsss', 'The first and last letters of a word should reamin in place with the inner letters sorted')
# scramble_words('card-carrying') #  'caac-dinrrryg', 'Only spaces separate words and punctuation should remain at the same place as it started')
# scramble_words("shan't") #  "sahn't", 'Punctuation should remain at the same place as it started')
# scramble_words('-dcba') #  '-dbca', 'Must handle special character at the start')
# scramble_words('dcba.') #  'dbca.', 'Must handle special character at the end')
# scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") # "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.")


# scramble_words('i') # 'i', 'Must handle single charater words')
# scramble_words('') #  '', 'Must handle empty strings')
# scramble_words('me') #  'me', 'Must handle 2 charater words')
# scramble_words('you') # 'you', 'Must handle 3 charater words')
