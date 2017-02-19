'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        currentNode = self 
        while currentNode.next != None:
            print(currentNode.val)
            currentNode = currentNode.next
        print(currentNode.val)

def addNode(root, newNode):
        currentNode = root
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = newNode

node1 = ListNode(2)
addNode(node1, ListNode(4))
addNode(node1, ListNode(3))

node2 = ListNode(5)
addNode(node2, ListNode(6))
addNode(node2, ListNode(4))

def addTwoNumbers(l1, l2):
    root = ListNode(l1.val + l2.val)
    currentL1 = l1
    currentL2 = l2
    current = root
    carry = False
    while (currentL1.next != None):
        if currentL2 == None and carry == False:
            addNode(currentL1)
        elif currentL2 == None and carry == True:
            addNode(currentL1 + 1)
        sum = currentL1.next.val + currentL2.next.val 
        if (sum < 10 and carry == False): 
            addNode(root, ListNode(sum))
        elif (sum + 1 < 10 and carry == True):
            addNode(root, ListNode(sum + 1))
            carry = False
        elif (sum + 1 > 10 and carry == True):
            addNode(root, ListNode(sum % 10))
        else:
            addNode(root, ListNode(sum % 10))
            carry = True
        currentL1 = currentL1.next
        currentL2 = currentL2.next
        current = current.next
    return root

node = addTwoNumbers(node1, node2)
node.printList()
