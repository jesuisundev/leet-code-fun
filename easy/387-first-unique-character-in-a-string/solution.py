class Solution(object):
    def firstUniqChar(self, s):
        """
        not optimal! to optimize
        """
        value_to_test = list(s)
        hashmap_uniq_char = {}

        for key in value_to_test:
            if key in hashmap_uniq_char.keys():
                hashmap_uniq_char[key] += 1
            else:
                hashmap_uniq_char[key] = 1

        for index, key in enumerate(value_to_test):
            if hashmap_uniq_char[key] == 1:
                return index

        return -1

print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))