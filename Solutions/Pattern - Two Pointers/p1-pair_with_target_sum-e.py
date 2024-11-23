class Solution:
    def search(self, arr, target_sum):
        start = 0
        end = len(arr) - 1

        while(start < end):
            sum = arr[start] + arr[end]
            if (sum == target_sum):
                return [start, end]
            elif (sum < target_sum):
                start += 1
            else:
                end -= 1
        
        return [-1, -1]