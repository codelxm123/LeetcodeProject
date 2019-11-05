class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head==None):
            return None
        if (head.next==None):
            return head
        newhead=head.next
        y=newhead.next
        newhead.next=head
        head=newhead
        pre=head.next
        while True:
            if (y and y.next):
                newy=y.next
                t=y.next.next
                newy.next=y
                y=newy
                pre.next=y
                pre=y.next
                y=t
            elif y:
                pre.next=y
                return head
            else:
                pre.next=None
                return head
        return head
