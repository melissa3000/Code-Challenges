
"""Using Lambdas as a mechanism for Open/Closed"""


spoken = lambda greeting: greeting + "."
shouted   = lambda greeting: greeting.upper() + "!"
whispered = lambda greeting: greeting.lower() + "."

greet = lambda style, msg: style(msg)

# print spoken("hello")
print greet(spoken, "hello")




spoken("Hello") #==>  "Hello."
shouted("Hello") #==>  "HELLO!"
whispered("Hello") #==> "hello."