# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        nop
        """
        before_head = ListNode(0)
        before_head.next = head
        
        previous_node, current_node = before_head, head

        while current_node:
            if current_node.val == val:
                previous_node.next = current_node.next
            else:
                previous_node = current_node

            current_node = current_node.next
        
        return before_head.next

fourth_node = ListNode(4)
third_node = ListNode(3, fourth_node)
second_node = ListNode(2, third_node)
head = ListNode(1, second_node)


print(Solution().removeElements(head, 3))

# - set up empty hashmap
# - one simple loop through the array o(n)
# - if number exist in hashmap => destroy it
# - if not add it
# - return fist index hashmap