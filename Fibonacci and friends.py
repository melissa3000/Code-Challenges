

def Xbonacci(signature,n):
    #your code here


    rge = len(signature)
    i = 0

    result = signature

    while (i + rge) < n:
        next_num = sum(signature[i:(i+rge)])
        result.append(next_num)
        i += 1
    return result



Xbonacci([1,1,1,1],10) #==[1,1,1,1,4,7,13,25,49,94]