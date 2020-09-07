from collections import deque

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    """
    simple dfs
    """
    def rangeSumBST(self, root, L, R):
        sum = 0
        stack = deque()
        stack.append(root)

        while stack:
            current_node = stack.pop()

            if current_node.val and current_node.val >= L and current_node.val <= R:
                sum += current_node.val
            
            if current_node.left:
                stack.append(current_node.left)
            
            if current_node.right:
                stack.append(current_node.right)
        
        return sum

#print(Solution().rangeSumBST([10,5,15,3,7,null,18], 7, 15))