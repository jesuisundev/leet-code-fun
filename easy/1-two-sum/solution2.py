class Solution(object):
    """
    better
    there is still a better solution
    """
    def twoSum(self, nums, target):
        hashTable = {num: index for index, num in enumerate(nums)}

        for index, number in enumerate(nums):
            diff = target - number
    
            if diff in hashTable and index != hashTable[diff]:
                return [index, hashTable[diff]]

        return []


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([0, 4, 3, 0], 0))
print(Solution().twoSum([-1,-2,-3,-4,-5], -8))
print(Solution().twoSum([1,3,4,2], 6))
