class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        allhead=head
        p=head
        prehead=None
        for _ in range(n):
            p=p.next
        while (p):
            p=p.next
            prehead=head
            head=head.next
        if (prehead==None):
            return allhead.next
        else:
            prehead.next=head.next
            return allhead

def createList(nums):
    L=ListNode(nums[0])
    tail=L
    for i in range(1,len(nums)):
        p=ListNode(nums[i])
        tail.next=p
        tail=p
    return L

def printList(l):
    if l==None:
        print()
    elif l.next:
        print("{}->".format(l.val),end="")
        printList(l.next)
    else:
        print(l.val)
