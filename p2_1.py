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

def printAns(resList):
    if resList==None:
        return
    printAns(resList.next)
    print(resList.val,end="")

str1=input()
str2=input()
n1=len(str1)
n2=len(str2)
l1=ListNode(int(str1[0]))
for i in range(1,n1):
    p=ListNode(int(str1[i]))
    p.next=l1
    l1=p
l2=ListNode(int(str2[0]))
for i in range(1,n2):
    p=ListNode(int(str2[i]))
    p.next=l2
    l2=p
m_solution=Solution()
printAns(l1)
print()
printAns(l2)
print()
res_list=m_solution.addTwoNumbers(l1,l2)
printAns(res_list)