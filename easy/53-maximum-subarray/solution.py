class Solution(object):
    def maxSubArray(self, nums):
        """
        using the max seen technique
        not optimal => should be using divide and conquer algo
        """
        tempSum = 0
        maxSum = nums[0]

        for index, num in enumerate(nums):
            tempSum = max(num, tempSum + num)
            maxSum = max(maxSum, tempSum)

        return maxSum

        
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
