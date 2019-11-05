# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1==None):
            return l2
        if (l2==None):
            return l1
        head=None
        l1h=l1
        l2h=l2
        if l1.val<=l2.val:
            head=l1
            l1h=l1.next
        else:
            head=l2
            l2h=l2.next
            
        p=head
        while (l1h):
            while (l2h and (l2h.val<l1h.val)):
                p.next=l2h
                p=p.next
                l2h=l2h.next
            p.next=l1h
            p=p.next
            l1h=l1h.next
            
        if (l2h):
            p.next=l2h
            p=p.next
            
        return head
