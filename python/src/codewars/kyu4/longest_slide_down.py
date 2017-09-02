def longest_slide_down(pyramid):
    for i,j in [(i,j) for i in range(len(pyramid)-2,-1,-1) for j in range(i+1)]:
        pyramid[i][j] +=  max([pyramid[i+1][j], pyramid[i+1][j+1]])

    return pyramid[0][0]
