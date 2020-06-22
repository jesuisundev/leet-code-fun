class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        firstPart = nums[:n]
        secondPart = nums[n:]
        result = []

        for i in range(n):
            result.append(firstPart[i])
            result.append(secondPart[i])

        return result
        

print(Solution().shuffle([1,2,3,4,4,3,2,1], 4))