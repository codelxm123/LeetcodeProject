# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add_num=0
        l3=None
        tail=None
        ans_head=None
        while (l1 or l2 or add_num==1):
            num=add_num
            if l1:
                num+=l1.val
                l1=l1.next
            if l2:
                num+=l2.val
                l2=l2.next
            if l3==None:
                l3=ListNode(num%10)
                tail=l3
                ans_head=l3
            else:
                new_node=ListNode(num%10)
                tail.next=new_node
                tail=new_node
            if (num>=10):
                add_num=1
            else:
                add_num=0
        return ans_head
