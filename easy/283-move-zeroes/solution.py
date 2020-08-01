class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        new_array = []
        i = 0

        for num in nums:
            if num == 0:
                i += 1
            else:
                new_array.append(num)

        for _ in range (0, i):
            new_array.append(0)

        return new_array

    def moveZeroesBetter(self, nums):
        lastNonZeroFoundAt = 0

        for index in range(0, len(nums)):
            print(lastNonZeroFoundAt, index)
            if nums[index] != 0:
                nums[lastNonZeroFoundAt] = nums[index]
                lastNonZeroFoundAt += 1
            print(nums)

        for index in range(lastNonZeroFoundAt, len(nums)):
            nums[index] = 0

        return nums


#print(Solution().moveZeroes([0,1,0,3,12]))
print(Solution().moveZeroesBetter([0,1,0,3,12]))