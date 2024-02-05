from node import Node

def insertion_sort_list(head):
    if not head or not head.next:
        return head

    sorted_head = Node(0)
    current = head

    while current:
        prev = sorted_head
        next_node = prev.next

        while next_node:
            if next_node.value > current.value:
                break
            prev = prev.next
            next_node = next_node.next

        temp = current.next
        current.next = next_node
        prev.next = current
        current = temp

    return sorted_head.next

head = Node(3)
head.next = Node(1)
head.next.next = Node(2)

sorted_head = insertion_sort_list(head)

current = sorted_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")