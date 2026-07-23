class Solution:

    def encode(self, strs):
        res = ""
        for i in strs:
            res += str(len(i))+ "#" + i
        return res
    
    def decode(self, s):
        # 2#we3#say1#:3#yes10#!@#$%^&*()
        i = 0 
        res = []
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j+1+length
        return res
