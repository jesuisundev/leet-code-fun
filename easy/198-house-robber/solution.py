class Solution(object):
    def rob(self, nums):
        previous_max = 0
        current_max = 0

        for index in range(0, len(nums)):
            temp = current_max
            current_max = max(previous_max + nums[index], current_max)
            previous_max = temp

        return current_max


print(Solution().rob([2,2,1]))
# print(Solution().rob([1,2,3,1]))
# print(Solution().rob([2,7,9,3,1]))
# print(Solution().rob([1,2]))
# print(Solution().rob([2,1,1,2]))
# print(Solution().rob([1,3,1,3,100]))
