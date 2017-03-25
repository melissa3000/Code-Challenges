"""
    >>> validate("MDZHB 85 596 KLASA 81 00 02 91")
    True
    """

import re

def validate(message):
  # Good luck!


    return bool(re.match(r"MDZHB\s\d{2}\s\d{3}\s[A-Z]+\s\d{2}\s\d{2}\s\d{2}\s\d{2}", message))






if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"