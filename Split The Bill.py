

def split_the_bill(x):
    average = sum(x.values()) / len(x.values())

    for key, value in x.items():
        x[key] = value - int(average)
    print x



split_the_bill({'A': 21.20, 'B': 15.4, 'C': 10}) # {'A': 5, 'B': 0, 'C': -5}

