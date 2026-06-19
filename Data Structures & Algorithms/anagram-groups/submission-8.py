# almost bruce force
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if not strs:
            return []

        space = {}
        for i in range(len(strs)):
            if i not in space.keys():
                space[i] = i
                for j in range(i+1, len(strs)):
                    if self.anagrams_indentifier(strs[j], strs[i]) and (j not in space.keys()):
                        space[j] = i
                    else:
                        continue

        holder = {}
        for key, value in space.items():
            if value not in holder.keys():
                holder[value] = [strs[key]]
            else:
                holder[value].append(strs[key])

        result = []
        for _, value in holder.items():
            result.append(value)    
        
        return result      


    def anagrams_indentifier(self, s, t):
        
        if len(s) != len(t):
            return False
        
        map = {}
        for i in range(len(s)):
            if s[i] in map.keys():
                map[s[i]] += 1
            else:
                map[s[i]] = 1
        
        for j in range(len(t)):
            if t[j] in map.keys():
                map[t[j]] -= 1
            else:
                map[t[j]] = 1 
        
        for word, cnt in map.items():
            if cnt != 0:
                return False
        return True

