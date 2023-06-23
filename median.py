# this code is going to return the median of 2 sorted arrays
# for input, we will be using 2 different arrays called arr1 and arr2

arr1 = [1,3,4,7]
arr2 = [9,23,45,65]
# now we will be merging the two arrays into a new array called merged_arr
merged_arr = arr1+arr2
#print (merged_arr)

# now we will need to sort this merged array
merged_arr = sorted(merged_arr)
print (merged_arr)

# now we will find the median. if there are an odd number of values in the array, we just need to find the middle
# value. if we have an even number of values, we need to find the 2 middle values and find the average

if len(merged_arr) % 2 == 1:
    middleIndex = int(len(merged_arr)/2)
    print (merged_arr[middleIndex])
else:
    index1 = int(len(merged_arr)/2)
    index2 = int(len(merged_arr)/2) - 1
    print ((merged_arr[index1]+merged_arr[index2])/2)
