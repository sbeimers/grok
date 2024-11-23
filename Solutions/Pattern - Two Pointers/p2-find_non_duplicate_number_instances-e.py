class Solution:
    def moveElements(self, arr):
        left, right, l, total = 0, 0, len(arr) - 1, 1
        while (right <= l):
            if arr[left] == arr[right]:
                right += 1
            else:
                left += 1
                arr[left] = arr[right]
                right += 1
                total += 1
        return total
