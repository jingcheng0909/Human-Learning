

n3 = 807
# split = list(str(n3))
# for i in range(len(split)):
#     split[i] = int(split[i])
results = list(map(int, list(str(n3))))
print(results)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# mine
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        d = ListNode()
        i = 0
        j = 0
        n1 = 0
        n2 = 0
        split = []
        while l1:
            n1 += pow(10, i) * l1.val
            i += 1
            l1 = l1.next

        while l2:
            n2 += pow(10, j) * l2.val
            j += 1
            l2 = l2.next

        n3 = n1 + n2
        l = list(map(int, list(str(n3))))
        l = l[::-1]
        self.head = ListNode(l[0])
        r = self.head
        p = self.head

        for i in l[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

        return r
