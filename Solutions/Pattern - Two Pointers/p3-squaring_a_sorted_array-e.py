class Solution:
    def makeSquares(self, arr):
        l = len(arr)
        a = [0 for x in range (l)]

        left, right, pos = 0, l-1, l-1

        while left < right:
            s_l = arr[left] ** 2
            s_r = arr[right] ** 2
            if (s_l >= s_r):
                a[pos] = s_l
                left += 1
            else:
                a[pos] = s_r
                right -= 1
            pos -= 1
        a[0] = arr[left] ** 2
        
        return a
