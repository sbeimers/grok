class Solution:
    def findMiddle(self, head):
        fast = head.next
        while (fast != None):
            fast = fast.next
            if (fast != None):
                fast = fast.next
            head = head.next
        return head