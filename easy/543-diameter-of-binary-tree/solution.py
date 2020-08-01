# Definition for a binary tree node.
from collections import deque

class Solution(object):
    class Solution(object):
        def diameterOfBinaryTree(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return 0
            
            if not root.left and not root.right:
                return 0

            length = 1
            seen = []
            my_queue = deque()

            my_queue.append(root)

            while my_queue:
                current_node = my_queue.popleft()
                seen.append(current_node)

                neighbors = self.get_neighbors(current_node, seen, my_queue)

                for neighbor in neighbors:
                    my_queue.append(neighbor)

                if len(neighbors):
                    length += 1
                else:
                    return length

    
    def get_neighbors(self, node, seen, my_queue):
        neighbors = []

        if node:
            if node.left and node.left not in seen and node.left not in my_queue:
                neighbors.append(node.left)

            if node.right and node.right not in seen and node.right not in my_queue:
                neighbors.append(node.right)

        return neighbors

print(Solution().diameterOfBinaryTree(root))