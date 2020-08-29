class Solution(object):
    def singleNumber(self, nums):
        """
        EZ PZ
        """
        myHashMap = {}

        for num in nums:
            if num in myHashMap:
                myHashMap.pop(num)
            else:
                myHashMap[num] = num
        
        return list(myHashMap.keys())[0]

print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([4,1,2,1,2]))
# - set up empty hashmap
# - one simple loop through the array o(n)
# - if number exist in hashmap => destroy it
# - if not add it
# - return fist index hashmap