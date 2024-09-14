# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def twolist(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<=l2.val:
            l1.next=self.twolist(l1.next,l2)
            return l1
        else:
            l2.next=self.twolist(l1,l2.next)
            return l2
    def partion(self,start,end,lists):
        if start==end:
            return lists[start]
        if start>end:
            return None
        mid=start +(end-start)//2
        l1=self.partion(start,mid,lists)
        l2=self.partion(mid+1,end,lists)
        return self.twolist(l1,l2)
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n=len(lists)
        if n==0:
            return None
        return self.partion(0,n-1,lists)

        