from collections import Counter

def fruit(reels, spins):

    score = 0

    pull = reels[0][spins[0]], reels[1][spins[1]], reels[2][spins[2]]
    pull = list(pull)

    d = Counter(pull)

    if d.get("Wild") == 3:
        score = 100
    elif d.get("Star") == 3:
        score = 90
    elif d.get("Bell") == 3:
        score = 80
    elif d.get("Shell") == 3:
        score = 70
    elif d.get("Seven") == 3:
        score = 60
    elif d.get("Cherry") == 3:
        score = 50
    elif d.get("Bar") == 3:
        score = 40
    elif d.get("King") == 3:
        score = 30
    elif d.get("Queen") == 3:
        score = 20
    elif d.get("Jack") == 3:
        score = 10
    elif d.get("Wild") == 2:
        score = 10
    elif d.get("Star") == 2 and d.get("Wild") == 1:
        score = 18
    elif d.get("Star") == 2 and d.get("Wild", 0) == 0:
        score = 9
    elif d.get("Bell") == 2 and d.get("Wild") == 1:
        score = 18
    elif d.get("Bell") == 2 and d.get("Wild", 0) == 0:
        score = 8
    elif d.get("Shell") == 2 and d.get("Wild") == 1:
        score = 14
    elif d.get("Shell") == 2 and d.get("Wild", 0) == 0:
        score = 7
    elif d.get("Seven") == 2 and d.get("Wild") == 1:
        score = 12
    elif d.get("Seven") == 2 and d.get("Wild", 0) == 0:
        score = 6
    elif d.get("Cherry") == 2 and d.get("Wild") == 1:
        score = 10
    elif d.get("Cherry") == 2 and d.get("Wild", 0) == 0:
        score = 5
    elif d.get("Bar") == 2 and d.get("Wild") == 1:
        score = 8
    elif d.get("Bar") == 2 and d.get("Wild", 0) == 0:
        score = 4
    elif d.get("King") == 2 and d.get("Wild") == 1:
        score = 6
    elif d.get("King") == 2 and d.get("Wild", 0) == 0:
        score = 3
    elif d.get("Queen") == 2 and d.get("Wild") == 1:
        score = 4
    elif d.get("Queen") == 2 and d.get("Wild", 0) == 0:
        score = 2
    elif d.get("Jack") == 2 and d.get("Wild") == 1:
        score = 2
    elif d.get("Jack") == 2 and d.get("Wild", 0) == 0:
        score = 1


    return score


#===========================================================================
# better solution:

SCORES = {'Wild': 10, 'Star': 9, 'Bell': 8, 'Shell': 7, 'Seven': 6,
          'Cherry': 5, 'Bar': 4, 'King': 3, 'Queen': 2, 'Jack': 1 }

def fruit(reels, spins):
    result = sorted( reels[i][spins[i]] for i in range(3) )

    if len(set(result)) == 1:
        return SCORES[result[0]] * 10

    elif len(set(result)) == 2:
        return SCORES[result[1]] * ((result[1] != result[2] == 'Wild') + 1)

    else:
        return 0

