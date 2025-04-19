class Solution:
    def searchTriplets(self, arr, target):
        count = 0
        arr.sort()

        for i in range (len(arr) - 2):
            start = i + 1
            end = len(arr) - 1

            while start < end:
                if arr[i] + arr[start] + arr[end] < target:
                    count += end - start
                    start += 1
                else:
                    end -= 1

        return count