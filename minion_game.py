def minion_game(string):

    Kevin_count = 0
    Stuart_count = 0

    for i in range(len(string)):
        if string[i] in "AEIOU":
            Kevin_count += len(string) - i
        else:
            Stuart_count += len(string) - i

    if Stuart_count > Kevin_count:
        print "Stuart", Stuart_count
    elif Kevin_count > Stuart_count:
        print "Kevin", Kevin_count
    else:
        print "Draw"


minion_game("BANANA")

