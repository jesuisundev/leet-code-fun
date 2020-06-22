class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        sum = 0
        
        for num in nums:
            sum = num + sum
            result.append(sum)
            
        return result

print(Solution().runningSum([1,2,3]))