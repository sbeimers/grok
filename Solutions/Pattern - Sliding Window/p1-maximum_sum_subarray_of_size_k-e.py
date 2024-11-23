import math
class Solution:
    def findMaxSumSubArray(self,k, arr):
        current = 0
        largest = 0
        for i in range (k):
            current += arr[i]
        largest = current
        for i in range (k, len(arr)):
            current += arr[i]
            current -= arr[i-k]
            if largest < current:
                largest = current
        return largest