class MySolution(object):
    def merge(self, nums1, m, nums2, n):
        tempNums = []

        while len(tempNums) != m + n:
            if nums1 and nums1[0] <= nums2[0] and nums1[0] != 0:
                tempNums.append(nums1.pop(0))
            else:
                tempNums.append(nums2.pop(0))

        return tempNums


class OneLinerSolution(object):
    """[summary]
    a[start:stop]      # items start through stop-1
    a[start:]          # items start through the rest of the array
    a[:stop]           # items from the beginning through stop-1
    a[:]               # a copy of the whole array
    a[start:stop:step] # start through not past stop, by step
    """
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2)

        return nums1


class TwoPointersSolution(object):
    def merge(self, nums1, m, nums2, n):
        # clone nums1
        nums1_clone = nums1[:m]
        # reset nums1
        nums1[:] = []
        # init pointers for nums1_copy and nums2.
        p1 = 0 
        p2 = 0

        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n: 
            if nums1_clone[p1] < nums2[p2]: 
                nums1.append(nums1_clone[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m: 
            nums1[p1 + p2:] = nums1_clone[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

        return nums1


print(MySolution().merge(
    [1,2,3,0,0,0],
    3,
    [2,5,6],
    3
))

print(OneLinerSolution().merge(
    [1,2,3,0,0,0],
    3,
    [2,5,6],
    3
))

print(TwoPointersSolution().merge(
    [1,2,3,0,0,0],
    3,
    [2,5,6],
    3
))