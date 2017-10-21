import functools
import operator

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def __init__(self):
		self.total = []
		
# 	def __init__(self):
# 		

	def averageOfLevels(self, t):
		"""
		:type root: TreeNode
		:rtype: List[float]
		"""
		# preorder(t)
		self.height = self.get_height(t)

		self.final = []
		for i in range(self.height):
			self.total = []
			self.printGivenLevel(t, i+1)
			self.final.append(self.mean(self.total))
		return self.final
	

	def preorder(self, tree):
		if tree:
			print(tree.val)
			preorder(tree.left)
			preorder(tree.right)

	def mean(self, l):
		return functools.reduce(operator.add, l)/len(l)	
	 
	def printGivenLevel(self, tree, level):
		if tree is None:
			return
		if level == 1:
			self.total.append(tree.val),
		elif level > 1 :
			self.printGivenLevel(tree.left , level-1)
			self.printGivenLevel(tree.right , level-1)
	 

	def get_height(self, tree):
		if tree is None:
			return 0
		else:
			lheight = self.get_height(tree.left)
			rheight = self.get_height(tree.right)
			if lheight > rheight:
				return lheight+1
			else:
				return rheight+1


t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.right = TreeNode(7)
t.right.left = TreeNode(15)
	
sol = Solution()
print(sol.averageOfLevels(t))
	




# print(mean([1,2,3]))