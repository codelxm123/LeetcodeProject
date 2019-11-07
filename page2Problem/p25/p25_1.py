# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (head==None):
            return None
        if (k==1):
            return head
        nextknode = head
        numk = 1
        while (numk < k):
            nextknode = nextknode.next
            if (nextknode == None):
                return head
            numk += 1

        numk=1
        p=head.next
        pre=head
        while (numk < k):
            pnext=p.next
            p.next=head
            head=p
            p=pnext
            numk += 1

        while True:
            pre.next=p
            thead=p
            nextknode=pre
            numk=0
            while (numk<k):
                nextknode=nextknode.next
                if (nextknode==None):
                    return head
                numk+=1
            numk=1
            mnode=thead
            p=thead.next
            tpre=pre
            while (numk < k):
                pnext = p.next
                p.next = thead
                thead = p
                p = pnext
                numk += 1
            tpre.next=thead
            pre=mnode
