

def get_sum(a,b):
    #good luck!
    if a == b:
        return a

    if a < b:
        result = sum(range(a, b + 1))
    elif b < a:
        result = sum(range(b, a + 1))
    return result

get_sum(0,1)