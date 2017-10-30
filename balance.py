"""
Each exclamation mark weight is 2; Each question mark weight is 3. Put two string
left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is more heavy,
return "Right"; If they are balanced, return "Balance"."""


#============ First Solution ====================================

# def balance(left, right):

#     lft_weight = 0
#     rt_weight = 0

#     for item in left:
#         if item == "!":
#             lft_weight += 2
#         elif item == "?":
#             lft_weight += 3

#     for item in right:
#         if item == "!":
#             rt_weight += 2
#         elif item == "?":
#             rt_weight += 3

#     if lft_weight == rt_weight:
#         print "Balance"
#     elif lft_weight > rt_weight:
#         print "Left"
#     else:
#         print "Right"



#============== More concise solution =================================

def balance(left, right):

    lft_weight = left.count("!") * 2 + left.count("?") * 3
    rt_weight = right.count("!") * 2 + right.count("?") * 3

    if lft_weight == rt_weight:
        print "Balance"
    elif lft_weight > rt_weight:
        print "Left"
    else:
        print "Right"





balance("","") #==> "Balance"
balance("!!","??") #==>  "Right"
balance("!??","?!!") #==>  "Left"
balance("!?!!","?!?") #==>  "Left"
balance("!!???!????","??!!?!!!!!!!") #==>  "Balance"