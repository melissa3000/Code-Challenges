
def order(sentence):
  # code here

    lst = sentence.split()
    result = []


    for i in range(1, 10):
        for word in lst:
            if str(i) in word:
                result.append(word)


    return " ".join(result)


order("is2 Thi1s T4est 3a") # ==>"Thi1s is2 3a T4est"