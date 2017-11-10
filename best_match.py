# Task

# "AL-AHLY" and "Zamalek" are the best teams in Egypt, but "AL-AHLY" always wins the matches between them. "Zamalek" managers want to know what is the best match they've played so far.

# The best match is the match they lost with the minimum goal difference. If there is more than one match with the same difference, choose the one "Zamalek" scored more goals in.

# Given the information about all matches they played, return the index of the best match (0-based). If more than one valid result, return the smallest index.

# Example

# For ALAHLYGoals = [6,4] and zamalekGoals = [1,2], the output should be 1.

# Because 4 - 2 is less than 6 - 1

# For ALAHLYGoals = [1,2,3,4,5] and zamalekGoals = [0,1,2,3,4], the output should be 4.

# The goal difference of all matches are 1, but at 4th match "Zamalek" scored more goals in. So the result is 4.

# Input/Output

# [input] integer array ALAHLYGoals

# The number of goals "AL-AHLY" scored in each match.
# [input] integer array zamalekGoals

# The number of goals "Zamalek" scored in each match. It is guaranteed that zamalekGoals[i] < ALAHLYGoals[i] for each element.
# [output] an integer

# Index of the best match.



def best_match(goals1, goals2):

    diff_lst = []
    diff_count = {}

    for i in range(len(goals1)):
        diff_lst.append(goals1[i] - goals2[i])

    lowest = min(diff_lst)
    lowest_index = diff_lst.index(min(diff_lst))
    # print "lowest: ", lowest
    # print "lowest_index: ", lowest_index

    for item in diff_lst:
        if diff_count.get(item, 0) == 0:
            diff_count[item] = 1
        else:
            diff_count[item] += 1

    # print "diff_count: ", diff_count


    if diff_count[lowest] == 1:
        return lowest_index
    # else:
    #     print

    # if diff_count.get(lowest)
    # else print index of max goals2 where count = lowest

    sorted_scores = sorted(goals2)
    print sorted_scores

    # if diff_lst[sorted_scores[-1]] == lowest:
    #     result = goals2.index(sorted_scores[-1])
    # elif diff_lst[sorted_scores[-2]] == lowest:
    #     result = goals2.index(sorted_scores[-2])


    # if diff_lst[goals2.index(max(goals2))] == lowest:
    #     result = goals2.index(max(goals2))
    # else


    # print result

# [1, 1, 1, 1, 1]



best_match([16, 10, 16, 15, 9, 17, 6, 6], [6, 9, 6, 7, 8, 8, 0, 3]) #==> 1

# best_match([6, 4],[1, 2]) #==>,1)
# best_match([1, 2, 3, 4, 5],[0, 1, 2, 3, 4]) #==>,4)



