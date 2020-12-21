class ListNode:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next


class merge:
    def solution(self, list1, list2, a, b):  # 给你两个链表 list1 和 list2 ，它们包含的元
        # 素分别为 n 个和 m 个。请你将 list1 中第 a 个节点到第 b 个节点删除，并将list2 接在被删除节点的位置。
        d1 = d2 = ListNode()  # d1会保留d2的值
        d2.next = list1
        for i in range(a):  # 将第一个指针遍历到a的位置
            d2 = d2.next

        d3 = d2.next  # 跳过一位，将a以后的位置赋值给d3
        k = b - a + 1
        for i in range(k):
            d3 = d3.next  # 跳过k位， 保留剩余的值
        d2.next = list2  # 将跳到a位的d2接到list2
        while d2.next:  # 遍历所有list2的值到尾部
            d2 = d2.next
        d2.next = d3  # 给尾部接上d3的值
        return d1.next  # 返回d1


'''        h = m = ListNode(None)
        h.next = list1
        i = a
        while i:
            i -= 1
            m = m.next
        n = m.next
        k = b - a + 1
        while k:
            k -= 1
            n = n.next
        m.next = list2
        while m.next:
            m = m.next
        m.next = n
        return h.next'''
