class Solution:
    def hasCycle(self, head):
        fast = head
        while fast.next != None and fast.next.next != None:
            head = head.next
            fast = fast.next.next
            if head == fast:
                return True

        return False
