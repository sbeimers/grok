class Solution:
    def findLength(self, s, k):
        lower, upper, cur_letters, best = 0, 0, 0, 0
        length = len(s)
        m = {}

        while (upper < length):
            if s[upper] not in m:
                m[s[upper]] = 0
                cur_letters += 1
            m[s[upper]] += 1
            
            while (cur_letters > k):
                if (m[s[lower]] == 1):
                    del m[s[lower]]
                    cur_letters -= 1
                else:
                    m[s[lower]] -= 1    
                lower += 1
            if (best < upper-lower+1):
                best = upper-lower+1
            upper += 1

        return best