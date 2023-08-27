height = [1,8,6,2,5,4,8,3,7]
maxArea = 0
maxHeight = max(height)
print (maxHeight)
for each in range(0,len(height)):
    for next in range(each+1,len(height)):
        width = next-each
        if height[next] <= height[each]:
            tempArea = width*height[next]
        else:
            tempArea = width * height[each]
        if tempArea > maxArea:
            maxArea = tempArea
print (maxArea)
