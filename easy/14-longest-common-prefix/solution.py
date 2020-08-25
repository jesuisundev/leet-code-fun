class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Not found, to rework
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        shortest_len =  len(min(strs, key=len))
        index = 0

        while index < shortest_len:
            current_char = strs[0][index]
            for i, current_sub_char in enumerate(strs):
                if current_sub_char[index] != current_char:
                    return strs[0][:index]
            index += 1

        return strs[0][:index]

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))

