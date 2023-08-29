class Solution:
    def groupAnagrams(self, strs):
        finalList = []
        tempList=[]
        x=0
        for each in range(len(strs)):
            tempList.append(strs[each])
            for next in range(each+1,len(strs)):
                if sorted(strs[each]) == sorted(strs[next]):
                    tempList.append(strs[next])
            for each in finalList:
                if sorted(each[0]) == sorted(tempList[0]):
                    x=1
            if x == 0:
                finalList.append(tempList)
            tempList = []
            x=0

        return (finalList)
