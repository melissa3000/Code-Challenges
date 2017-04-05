"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""

    operators = []
    numbers = []

    for char in s:
        if char in '+-/*':
            operators.append(char)
        if char in '1234567890':
            numbers.append(char)

    num2 = int(numbers.pop())

    while operators:

        operator = operators.pop()
        num1 = int(numbers.pop())

        if operator == "+":
            num2 = num1 + num2

        elif operator == "-":
            num2 = num1 - num2

        elif operator == "*":
            num2 = num1 * num2

        elif operator == "/":
            num2 = num1/num2

    return num2


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"
