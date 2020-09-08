class Solution(object):
    def missingNumber(self, nums):
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            return 0
        else:
            my_hash_map = {num : index for index, num in enumerate(nums)}
            for index in range(0, len(nums)):
                if my_hash_map.get(index) is None:
                    return index

            return len(nums)

print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
print(Solution().missingNumber([0,1]))
