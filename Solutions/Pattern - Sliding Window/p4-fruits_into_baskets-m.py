class Solution:
    def findLength(self, fruits):
        m = {}
        best, current, num_dif, lower = 0, 0, 0, 0
        length = len(fruits)

        for i in range (0, length):
            if (fruits[i] not in m):
                m[fruits[i]] = 0
                num_dif += 1
            m[fruits[i]] += 1
            current += 1

            while num_dif > 2:
                if (m[fruits[lower]] == 1):
                    del m[fruits[lower]]
                    num_dif -= 1
                else:
                    m[fruits[lower]] -= 1
                lower += 1
                current -= 1

            if (best < current):
                best = current
        return best
