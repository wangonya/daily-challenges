# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        _sum = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            _sum = carry + l1_val + l2_val

            # update carry for next calculation
            carry = 1 if _sum > 9 else 0

            # update sum if > 9
            _sum = _sum if _sum < 10 else _sum % 10

            # insert _sum to llist
            self.insert(_sum)

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if carry:
            self.insert(carry)

        self.reverse()

        return self.head


# if __name__ == '__main__':
#     l1 = ListNode(1, 2)
#     l2 = ListNode(5, 6)
#     s = Solution()
#     print(Solution.addTwoNumbers(s, l1, l2))

# result = ListNode(0)
# result_tail = result
# carry = 0

# while l1 or l2 or carry:
#     val1  = (l1.val if l1 else 0)
#     val2  = (l2.val if l2 else 0)
#     carry, out = divmod(val1+val2 + carry, 10)

#     result_tail.next = ListNode(out)
#     result_tail = result_tail.next

#     l1 = (l1.next if l1 else None)
#     l2 = (l2.next if l2 else None)

# return result.next
