class Solution:
    def findLength(self, arr, k):
        length = len(arr)
        m = {0:0, 1:0}
        best, lower = 0, 0
        for i in range (0, length):
            m[arr[i]] += 1
        
            while (m[0] > k):
                m[arr[lower]] -= 1
                lower += 1
        
            if best < i-lower+1:
                best = i-lower+1
        return best
