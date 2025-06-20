# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        protect_head = ListNode()
        while head is not None:
            tmp_node = ListNode(head.val, protect_head.next)
            protect_head.next = tmp_node
            head = head.next
        return protect_head.next
