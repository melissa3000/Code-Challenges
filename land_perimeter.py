"""Given an array arr of strings complete the function landPerimeter by
calculating the total perimeter of all the islands. Each piece of land will be
marked with 'X' while the water fields are represented as 'O'. Consider each
tile being a perfect 1 x 1piece of land. Some examples for better visualization:

['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']

 ['XOOXO', 'XOOXO', 'OOOXO', 'XXOXO', 'OXOOO']

should return: "Total land perimeter: 24"

['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']

 should return: "Total land perimeter: 18"
 """

def land_perimeter(arr):

    # x_loc = []

    # for island in arr:
    #     for index, char in enumerate(island):
    #         if char == 'X':
    #             x_loc.append(index)
    # print x_loc

    perim = 0


    for i in range(len(arr)):
        if arr[i][i] == 'X':
            square = 4
            if arr[i][i + 1] == 'X':
                square -= 1
            if arr[i + 1][i] == 'X':
                square -= 1
            if arr[i - 1][i] == 'X':
                square -= 1
            # else:
            #     square = 0
        perim += square
    print perim


    # print [i for i, j in zip(arr[0], arr[1]) if i == j]



    # for x in word, perim = 4, if next index position is x then subtract 1, if
    # x in same position in next word, subtract 1 again, if x in same position in
    # previous word, subtract 1


land_perimeter(['XOOXO', 'XOOXO', 'OOOXO', 'XXOXO', 'OXOOO']) # ==> "Total land perimeter: 24"

land_perimeter(['XOOO', 'XOXO', 'XOXO', 'OOXX', 'OOOO'])


