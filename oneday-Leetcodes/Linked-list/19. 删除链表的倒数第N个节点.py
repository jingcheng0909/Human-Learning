# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 先将原内容提取
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.pop(-n)
        # 如果列表为空 返回空链表
        if len(l) == 0:
            return head

        # 创建新链表来
        self.head = ListNode(l[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in l[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

        return r


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 快慢指针
        d = ListNode(0, head)
        # 先设定d
        first = head
        second = d
        # first先走n步
        for i in range(n):
            first = first.next
        # first和second一起走到first结尾
        while first:
            first = first.next
            second = second.next
        # second跳过下一个节点
        second.next = second.next.next
        return d.next

