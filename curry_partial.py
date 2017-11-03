"""Currying and partial application are two ways of transforming a function into
another function with a generally smaller arity. While they are often confused
with each other, they work differently. The goal is to learn to differentiate them.

Given:
def add(x, y, z):
  return x + y + z

add(1, 2, 3) # => 6

But we can create a curried version of add(a, b, c)function:
curriedAdd = lambda a: (lambda b: (lambda c: add(a,b,c)))

curriedAdd(1)(2)(3) # => 6

And:
partialAdd = lambda a: (lambda *args: add(a,*args))

partialAdd(1)(2, 3) # => 6

"""

# from operator import add

def curry_partial(f,*initial_args):
#   "Curries and partially applies the initial arguments to the function"

    def add(*args):
        # return add(args)

        sum = 0
        for n in args:
            sum += n
        return sum

    f = add(*initial_args)