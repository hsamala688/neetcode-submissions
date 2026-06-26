# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        '''
        curr = head

        hash_map = {}

        while curr != None:

            if hash_map.get(curr.val, 0) > 1:

                return True

            hash_map[curr.val] = hash_map.get(curr.val, 0) + 1

            curr = curr.next

        return False
        '''

        slow, fast = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False