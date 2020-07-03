class Solution(object):
    def isAlienSorted(self, words, order):
        """
        not working solution since i did not get the problem at the first place
        to redo (lexicographicaly)
        """
        # max_index_seen = 0
        # order_hash_map = self._buildHashMap(order)

        # for word in words:
        #     max_index_seen = 0

        #     for letter in word:
        #         found_index_letter = order_hash_map[letter]

        #         if found_index_letter:
        #             if found_index_letter < max_index_seen:
        #                 return False
        #             else:
        #                 max_index_seen = found_index_letter
        #         else:
        #             return False

        # return True

    # def _buildHashMap(self, items):
    #     hashMap = {}

    #     for index, num in enumerate(items):
    #         hashMap[num] = index + 1

    #     return hashMap
 
        order_index = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            # Find the first difference word1[k] != word2[k].
            for k in range(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False
        
        return True




        
        

print(Solution().isAlienSorted(
    ["hello","leetcode"],
    "hlabcdefgijkmnopqrstuvwxyz"
))



print(Solution().isAlienSorted(
    ["word","world","row"],
    "worldabcefghijkmnpqstuvxyz"
))