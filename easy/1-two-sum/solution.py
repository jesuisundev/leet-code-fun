class Solution(object):
    def twoSum(self, nums, target):
        """
        using hashmap to avoid o(n2)
        """
        builtHashMap = self._buildHashMap(nums)
        result = []

        for index, num in enumerate(nums):
            toFound = target - num
            indexFound = builtHashMap.get(toFound)

            if indexFound and indexFound is not index:
                return [index, indexFound]


        return result


    def _buildHashMap(self, nums):
        hashMap = {}

        for index, num in enumerate(nums):
            hashMap[num] = index

        return hashMap

    
    def twoSumBetterSolution(self, nums, target):
        hashMap = {}

        for index, num in enumerate(nums):
            toFound = target - num

            if toFound not in hashMap:
                hashMap[num] = index
            else:
                return [hashMap[toFound], index]

        
print(Solution().twoSumBetterSolution(
    [2, 7, 11, 15],
    9
))


print(Solution().twoSumBetterSolution(
    [0, 4, 3, 0],
    0
))

print(Solution().twoSumBetterSolution(
    [-1,-2,-3,-4,-5],
    -8
))

print(Solution().twoSumBetterSolution(
    [1,3,4,2],
    6
))

