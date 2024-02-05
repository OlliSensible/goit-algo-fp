from node import Node

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev

my_list = Node(1)
my_list.next = Node(2)
my_list.next.next = Node(3)
my_list.next.next.next = Node(4)
my_list.next.next.next.next = Node(5)

current = my_list
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

reversed_list = reverse_list(my_list)

current = reversed_list
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")