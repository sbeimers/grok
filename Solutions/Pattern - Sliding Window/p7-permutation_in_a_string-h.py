class Solution:
    def findPermutation(self, s, pattern):
        length = len(s)
        p, m = {}, {}
        cur, lower = 0, 0
        lp = len(pattern)
        for char in pattern:
            if (char not in p):
                p[char] = 0
            p[char] += 1
        
        for i in range(0, length):
            if s[i] not in m:
                m[s[i]] = 0
            m[s[i]] += 1
            cur += 1

            if (cur > lp):
                if m[s[lower]] == 1:
                    del m[s[lower]]
                else:
                    m[s[lower]] -= 1
                lower += 1
            
            if m == p:
                return True
        return False
