# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head
        prev = None

        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

















        #brtue force soltuion
        # temp = head
        # stack = []

        # while temp is not None:
        #     stack.append(temp.val)
        #     temp = temp.next

        # temp = head

        # while temp is not None:
        #     a = stack.pop()
        #     temp.val = a
        #     temp = temp.next

        # return head

