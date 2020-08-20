# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        EZ PZ
        """
        linked_list_hashmap = self._build_hashmap_from_linked_list(head)

        begin_pointer = 0
        end_pointer = len(linked_list_hashmap) - 1

        while begin_pointer != end_pointer and end_pointer >= 0 and begin_pointer <= len(linked_list_hashmap) - 1:
            if linked_list_hashmap[begin_pointer] == linked_list_hashmap[end_pointer]:
                begin_pointer += 1
                end_pointer -= 1
            else:
                return False

        return True

    def _build_hashmap_from_linked_list(self, node):
        myHashmap = {}
        index = 0

        if node:
            while node.next is not None:
                myHashmap[index] = node.val
                node = node.next
                index += 1

            myHashmap[index] = node.val

        return myHashmap


head = ListNode(1)
second = ListNode(2)
head.next = second
third = ListNode(2)
second.next = third
fourth = ListNode(1)
third.next = fourth

print(Solution().isPalindrome(head))