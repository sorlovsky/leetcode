# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
    	carry = 0
    	root = v1 = v2 = 0
    	while carry or v1 or v2:
    		if v1:
    			val1 = v1.val
    			v1 = v1.next
    		if v2:
    			val2 = v2.val
    			v2 = v2.next
    		val, carry = divmod((carry+v1.val+v2.val)/10)

    		
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pass

a = ListNode(5)
b = ListNode(2)
a.next = b
c = ListNode(2)
b.next = c

d = ListNode(4)
e = ListNode(3)
d.next = e
f = ListNode(2)
d.next = f