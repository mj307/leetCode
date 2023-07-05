# this code will take a list, sort it, and remove elements that occur more than twice
nums = [3,3,3,4,1,1,1,1,1,2,2]
nums = sorted(nums)
print (nums)
# count stores how many times a certain element is in the list
count = 0
# number stores the new number if there is a change in element value
number = nums[0]
# index stores the value of the repeat elements, so it knows what values to remove
index = 0
for each in nums[:]:
    if each == number:
        count += 1
    elif each != number:
        number = each
        count = 1
    if count > 2:
        nums.pop(index)
        index -= 1
    index += 1
print (nums)

