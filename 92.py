# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if left < right:
            counter = 1
            current = head
            thePrev = beforeFirstNode = firstNode = None
            while counter <= right:
                if counter < left - 1:
                    current = current.next
                elif counter == left - 1:
                    beforeFirstNode = current
                    current = current.next
                elif counter == left:
                    firstNode = current
                    thePrev = current
                    current = current.next
                elif counter > left:
                    temp = current.next
                    current.next = thePrev
                    thePrev = current
                    current = temp
                counter += 1
            firstNode.next = current
            if beforeFirstNode == None:
                head = thePrev
            else:
                beforeFirstNode.next = thePrev
        return head
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        