

def calculate_years(principal, interest, tax, desired):

    years = 0

    if principal == desired:
        return years

    while principal < desired:
        amt_taxed = principal * interest
        after_tax = amt_taxed * (1 - tax)
        principal += after_tax
        years += 1
        # print "principal: ", principal
    return years

# calculate_years(1000,0.01625,0.18,1200) # ==> 14