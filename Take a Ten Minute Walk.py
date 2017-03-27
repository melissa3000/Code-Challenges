def isValidWalk(walk):
    #determine if walk is valid
    if len(walk) != 10:
        return False

    if walk.count('w') != walk.count('e'):
        return False
    if walk.count('n') != walk.count('s'):
        return False
    else:
        True




#walk must be exactly 10 min
# every n - s must be same num
# every e - w must be same num
# len lst must be 10
