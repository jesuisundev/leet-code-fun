from collections import deque 

class Solution(object):
    """
    - need more work
    """
    def hasPath(self, maze, start, destination):
        queue = deque()
        seen = list()
        destination = tuple(destination)
        start = tuple(start)

        queue.append(start)

        while queue:
            currentNodeRow, currentNodeColumn = queue.popleft()
            
            if (currentNodeRow, currentNodeColumn) == destination:
                return True

            seen.append((currentNodeRow, currentNodeColumn))

            for validAdjacentNode in self.validAdjacentNodes((currentNodeRow, currentNodeColumn), seen, maze):
                queue.appendleft(validAdjacentNode)

        return False


    def validAdjacentNodes(self, node, seen, maze):
        directions_offset = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        originRow, originColumn = node

        for row_offset, column_offset in directions_offset:
            next_row, next_col = (originRow + row_offset, originColumn + column_offset)

            if self.isValidNode(next_row, next_col, maze) and (next_row, next_col) not in seen:
                yield (next_row, next_col)


    def isValidNode(self, row, column, maze):
        if column >= 0 and row >=0 and column < len(maze) and row < len(maze) and maze[row][column] == 0:
            return True
        return False


print(Solution().hasPath(
    [
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]
    ],
    [0,4],
    [4,4]
))

print(Solution().hasPath(
    [
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]
    ],
    [0,4],
    [3,2]
))
