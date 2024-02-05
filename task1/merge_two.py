from node import Node

def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    tail = dummy
    while head1 and head2:
        if head1.value < head2.value:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    if head1:
        tail.next = head1
    else:
        tail.next = head2
    return dummy.next

list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

merged_list = merge_sorted_lists(list1, list2)

current = merged_list
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")