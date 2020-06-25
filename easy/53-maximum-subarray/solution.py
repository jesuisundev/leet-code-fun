class Solution(object):
    def maxSubArray(self, nums):
        """
        using the max seen technique
        not optimal => should be using divide and conquer algo

        Time complexity : O(n) since it's one pass along the array.
        Space complexity : O(1), since it's a constant space solution.
        (constant space just means the memory you use does not depends on the size of the input.)
        """
        tempSum = 0
        maxSum = nums[0]

        for num in nums:
            tempSum = max(num, tempSum + num)
            maxSum = max(maxSum, tempSum)

        return maxSum

        
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))