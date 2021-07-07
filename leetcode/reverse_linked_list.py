class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        pass

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(f"val = {printval.val}")
            print(f"next = {printval.next.val}")
            printval = printval.next


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    s = Solution()

    for i, n in enumerate(x):
        print(f"i,n = {i,n}")
        if i == 0:
            s.head = ListNode(n)
        else:
            s.head.next = ListNode(n)

    s.listprint()
