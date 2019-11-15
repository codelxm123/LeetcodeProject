from Queue import PriorityQueue
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        m_queue=PriorityQueue()
        for node in lists:
            if node:
                m_queue.put((node.val,node))
        tail=ListNode(0)
        head=tail
        while not m_queue.empty():
            now_val,now_node=m_queue.get()
            p=ListNode(now_val)
            tail.next=p
            tail=p
            now_node=now_node.next
            if (now_node):
                m_queue.put((now_node.val,now_node))
        return head.next
