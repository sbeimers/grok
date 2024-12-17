class Solution:
    def findLength(self, s, k):
        m = {}
        best, current, lower, letter = 0, 0, 0, 0
        length = len(s)

        for i in range (0, length):
            if (s[i] not in m):
                m[s[i]] = 0
            m[s[i]] += 1
            current += 1

            letter = max(m, key=m.get)
            
            while ((sum(m.values()) - m[letter]) > k):
                if (m[s[lower]] == 1):
                    del m[s[lower]]
                else:
                    m[s[lower]] -= 1
                current -= 1
                lower += 1
                letter = max(m, key=m.get)

            if best < current:
                best = current
        return best
