class Solution:
    def searchRange(self, nums, target):
        indexList = []
        for each in range(len(nums)):
            if nums[each] == target:
                indexList.append(each)
        if len(indexList) == 0:
            return ([-1,-1])
        if len(indexList)==1:
            return ([indexList[0],indexList[0]])
        return ([indexList[0],indexList[-1]])