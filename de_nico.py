# Write a function de_nico() that accepts two parameters:

# key/$key - string consists of unique letters and digits
# message/$message - string with encoded message
# and decodes the message using the key.

# First create a numeric key basing on the provided key by assigning each letter position in which it is located after setting the letters from key in an alphabetical order.

# For example, for the key crazy we will get 23154 because of acryz (sorted letters from the key).
# Let's decode cseerntiofarmit on using our crazy key.

def de_nico(key,msg):

    sorted_key_list = sorted(key)
    key_order = []

    for char in key:
        key_order.append(sorted_key_list.index(char))

    result = ''
    start = 0
    stop = len(key)

    while start < len(msg):
        segments_to_decode = msg[start : stop]
        for index in key_order:
            if index < len(segments_to_decode):
                result += segments_to_decode[index]
        start = stop
        stop += len(key)

    return result.strip()




de_nico("crazy", "cseerntiofarmit on  ") #=> "secretinformation"
# de_nico("abc", "abcd") #=> "abcd"
# de_nico("ba", "2143658709") #=> "1234567890"
# de_nico("key", "eky") #=> "key"





