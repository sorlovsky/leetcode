import functools
import operator

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

total = []

def preorder(tree):
	if tree:
		print(tree.val)
		preorder(tree.left)
		preorder(tree.right)

def mean(l):
	return functools.reduce(operator.add, l)/len(l)	
 
def printGivenLevel(tree, level):
    if tree is None:
        return
    if level == 1:
        total.append(tree.val),
    elif level > 1 :
        printGivenLevel(tree.left , level-1)
        printGivenLevel(tree.right , level-1)
 

def height(tree):
	if tree is None:
		return 0
	else:
		lheight = height(tree.left)
		rheight = height(tree.right)
		if lheight > rheight:
			return lheight+1
		else:
			return rheight+1

def level_order(tree):
	if tree:
		pass

t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.right = TreeNode(7)
t.right.left = TreeNode(15)

height = height(t)

final = []
for i in range(height):
	total = []
	printGivenLevel(t, i+1)
	final.append(mean(total))

print(final)



# print(mean([1,2,3]))