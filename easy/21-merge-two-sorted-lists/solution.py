class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        Recursive solution
        We model the above recurrence directly, first accounting for edge cases. 
        Specifically, if either of l1 or l2 is initially null, there is no merge to perform, so we simply return the non-null list. 
        Otherwise, we determine which of l1 and l2 has a smaller head, and recursively set the next value for that head to the next merge result. 
        Given that both lists are null-terminated, the recursion will eventually terminate.
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
