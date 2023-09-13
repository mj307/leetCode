# row_limit = row-1 # lets you know if a move is exceeding the length of the chessboard
# col_limit = column - 1
# starting position is row, column
# 8 different combinations to where a piece can move:
# 2 right 1 up,
# 2 right 1 down,
# 2 left 1 down,
# 2 left 1 up
# 2 up 1 left
# 2 up 1 right
# 2 down 1 left
# 2 down 1 right

# given the starting point of the knight (row, column), figure out all the possible points the knight can be after the first move
# then create a list, but don't double count the points. only add to the list if the points are within the board range
# then iterate through the length of the list to find out the new points. delete this point from the list, and then add the new points in at the very end.
# keep deleting and adding the new points until we are on iteration k.
# then find the length of the list.
# take that length and divide it by k^8
def knightProbability(n, k, row, column):
    pointList = [[row,column]]
    smallList = [[row,column]]
    for each in range(0,k):
        print (pointList)
        pointList.append('x')
        for each1 in pointList[0:pointList.index('x')]:
            row = each1[0]
            column = each1[1]
            if row + 2 < n and column + 1 < n and row + 2 > -1 and column + 1 > -1:
                if [row+2,column+1] not in pointList:
                    pointList.append([row+2,column+1])
                elif each == k-1:
                    pointList.append([row + 2, column + 1])

            if row - 2 < n and column + 1 < n and row - 2 > -1 and column + 1 > -1:
                if [row-2,column+1] not in pointList:
                    pointList.append([row-2,column+1])
                elif each == k-1:
                    pointList.append([row - 2, column + 1])
            if row + 2 < n and column - 1 < n and row + 2 > -1 and column - 1 > -1:
                if [row + 2, column - 1] not in pointList:
                    pointList.append([row + 2, column - 1])
                elif each == k-1:
                    pointList.append([row + 2, column - 1])

            if row - 2 < n and column - 1 < n and row - 2 > -1 and column - 1 > -1:
                if [row - 2, column - 1] not in pointList:
                    pointList.append([row - 2, column - 1])
                elif each == k-1:
                    pointList.append([row - 2, column - 1])

            if row + 1 < n and column + 2 < n and row + 1 > -1 and column + 2 > -1:
                if [row + 1, column + 2] not in pointList:
                    pointList.append([row + 1, column + 2])
                elif each == k-1:
                    pointList.append([row + 1, column + 2])

            if row - 1 < n and column + 2 < n and row - 1 > -1 and column + 2 > -1:
                if [row - 1, column + 2] not in pointList:
                    pointList.append([row - 1, column + 2])
                elif each == k-1:
                    pointList.append([row - 1, column + 2])

            if row + 1 < n and column - 2 < n and row + 1 > -1 and column - 2 > -1:
                if [row + 1, column - 2] not in pointList:
                    pointList.append([row + 1, column - 2])
                elif each == k-1:
                    pointList.append([row + 1, column - 2])

            if row - 1 < n and column - 2 < n and row - 1 > -1 and column - 2 > -1:
                if [row - 1, column - 2] not in pointList:
                    pointList.append([row - 1, column - 2])
                elif each == k-1:
                    pointList.append([row - 1, column - 2])
        index = pointList.index('x')
        pointList = pointList[index+1:]
        #print("###")
        print (pointList)
    numerator = len(pointList)
    return numerator/(8**k)

print (knightProbability(3,3,0,0))

l = [1,2,3,4,5]
index = l.index(2)
#print (l[index+1:])