class Solution(object):
    def majorityElement(self, nums):
        my_hash_map = self.build_hashmap(nums)

        for num in my_hash_map:
            if my_hash_map[num] >= (len(nums) / float(2)):
                return num

    def build_hashmap(self, nums):
        local_hash_map = {}

        for num in nums:
            if local_hash_map.get(num):
                local_hash_map[num] += 1
            else:
                local_hash_map[num] = 1

        return local_hash_map


        
print(Solution().majorityElement([3,2,3]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))
