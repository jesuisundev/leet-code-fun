# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # create previous, next pointer
        previousNode = None
        currentNode = head

        while currentNode is not None:
            # Remember the next node
            nextNode = currentNode.next

            # actual reversing (with empty previous first time)
            currentNode.next = previousNode

            # advance previous and current
            previousNode = currentNode
            currentNode = nextNode

        return previousNode