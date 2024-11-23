class Solution:
    def findCycleStart(self, head):
        start = head

        k = self.findCycleLength(head)
        ahead = start
        for i in range (k):
            ahead = ahead.next
        while (ahead != start):
            start = start.next
            ahead = ahead.next
        return start

    def findCycleLength(self, head):
        fast = head.next

        while fast != head:
            fast = fast.next.next
            head = head.next
        
        fast = fast.next
        count = 1
        while fast != head:
            fast = fast.next
            count += 1
        return count
