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
# addNode(node2, ListNode(4))

def addTwoNumbers(l1, l2):
	root = ListNode(l1.val + l2.val)
	currentL1 = l1
        currentL2 = l2
        current = root
        carry = False
        while (currentL1.next != None) or (currentL2.next != None):
            print("hello")
            # if currentL2.next == None and carry == False:
                # addNode(root, ListNode(currentL1.next.val))
            # elif currentL2.next == None and carry == True:
                # addNode(root, ListNode(currentL1.next.val + 1))
                
            # if currentL1.next == None and carry == False:
                # addNode(root, ListNode(currentL2.next.val))
            # elif currentL1.next == None and carry == True:
                # addNode(root, ListNode(currentL2.next.val + 1))
                
            # if currentL1 == None and carry == False:
            #     addNode(root, ListNode(currentL2))
            # elif currentL1 == None and carry == True:
            #     addNode(root, ListNode(currentL2 + 1))
                
            else:
                if hasattr(currentL1.next, 'val') and hasattr(currentL2.next, 'val'):
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
            if !(hasattr(currentL1, 'next')) and hasattr(currentL2, 'next'):
                break
        if hasattr(currentL1, 'next'):
            while (currentL1.next != None):
                if carry == False:
                    addNode(root, ListNode(currentL1.next.val))
                else:
                    if currentL1.next.val == 9:
                        addNode(root, ListNode(0))
                    else:
                        addNode(root, ListNode(currentL1.next.val))


        return root
node = addTwoNumbers(node1, node2)
node.printList()
