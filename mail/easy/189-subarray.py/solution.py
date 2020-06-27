class Solution(object):
    def subArray(self, nums):
        """
        Given an array of elements, return the length of the longest subarray where all its elements are distinct.

        For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

        found solution using built-int data structure set
        Time complexity : 0(n)  (linear time)
        
        """
        biggestSeen = 0
        currentStreak = set()

        for num in nums:
            if num in currentStreak:
                currentStreak = set()
                currentStreak.add(num)
            else:
                currentStreak.add(num)
                if biggestSeen < len(currentStreak):
                    biggestSeen = len(currentStreak)

        return biggestSeen


print(Solution().subArray([5, 1, 3, 5, 2, 3, 4, 1]))
