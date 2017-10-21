# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_l = None
        l = ListNode(l1.val+l2.val)
        while l1.next !=  None:
        	l1 = l1.next
        	l2 = l2.next
        	# print(l1.val, l2.val)
        	new_l = ListNode(l1.val+l2.val)
        	new_l.next = l
        	# print(l1.val)

        return new_l	

l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(5)

l2 = ListNode(3)
l2.next = ListNode(2)
l2.next.next = ListNode(5)

l = addTwoNumbers(l1, l2)

print(l.val)
while l.next != None:
	print(l.val)
	l = l.next