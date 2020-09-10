class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        hash_map_of_s = self.build_hash_map(s)
        hash_map_of_t = self.build_hash_map(t)
        
        for key_from_s in hash_map_of_s:
            if hash_map_of_t.get(key_from_s) is None:
                return False
            elif hash_map_of_t[key_from_s] != hash_map_of_s[key_from_s]:
                return False

        return True
    
    def build_hash_map(self, string):
        local_hash_map = {}
        
        for _, char in enumerate(string):
            if local_hash_map.get(char) is None:
                local_hash_map[char] = 0
            else:
                local_hash_map[char] += 1
                
        return local_hash_map