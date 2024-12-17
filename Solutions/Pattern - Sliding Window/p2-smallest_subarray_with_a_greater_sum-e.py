import math

class Solution:
    def findMinSubArray(self, s, arr):
        current, best, length = arr[0], math.inf, len(arr)
        lower, higher = 0, 0

        if (current >= s):
            best = higher-lower+1

        while (lower < length - 1 and higher < length):
            if (current < s):
                higher += 1
                if (higher == length):
                    break
                current += arr[higher]
            elif (current >= s):
                current -= arr[lower]
                lower += 1
            
            if (current >= s and higher-lower+1 < best):
                best = higher-lower+1
        
        if best == math.inf:
            return 0
        return best
