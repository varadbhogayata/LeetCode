# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ans = []
        # iterate through list and store values in list
        while head:
            ans.append(head.val)
            head = head.next
        return ans == ans[::-1]