"""Write a function dirReduc which will take an array of strings and returns an
array of strings with the needless directions removed (W<->E or S<->N side by side)."""

def dirReduc(arr):

    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}

    result = []

    for item in arr:
        if result and result[-1] == opposites[item]:
            result.pop()
        else:
            result.append(item)
    print result



dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) #=> ["WEST"]
dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]) #=> []
dirReduc(["NORTH", "WEST", "SOUTH", "EAST"])