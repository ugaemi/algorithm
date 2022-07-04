"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Brute Force

        Time complexity: O(N log N)
        Space complexity: O(N)
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Optimize Approach 2 by heapq
        """
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode()
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next
