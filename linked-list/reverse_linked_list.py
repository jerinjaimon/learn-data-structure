"""
Given the head of a singly linked list, reverse the list, and
return the reversed list.
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        curr = head
        prev_nord = None
        while curr:
            next_nord = curr.next
            curr.next = prev_nord
            prev_nord = curr
            curr = next_nord
        return prev_nord
