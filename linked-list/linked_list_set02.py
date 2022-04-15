
"""
Design your implementation of the linked list.

You can choose to use a singly or doubly linked list.

A node in a singly linked list should have two attributes: val and next.
val is the value of the current node, and next is a pointer/reference
to the next node.
If you want to use the doubly linked list, you will need one more attribute
prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.

int get(int index) Get the value of the indexth node in the linked list.
If the index is invalid, return -1.

void addAtHead(int val) Add a node of value val before the first element of
the linked list. After the insertion, the new node will be the
first node of the linked list.

void addAtTail(int val) Append a node of value val as the last element of the
linked list.

void addAtIndex(int index, int val) Add a node of value val before the
indexth node in the linked list. If index equals the length of the linked list,
the node will be appended to the end of the linked list. If index is
greater than the length, the node will not be inserted.

void deleteAtIndex(int index) Delete the indexth node in the linked list,
if the index is valid.


Explanation:
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
"""


class Nord:
    """Nord class."""

    def __init__(self, val=None, next=None):
        """Initialize nord with value."""
        self.val = val
        self.next = next


class MyLinkedList:
    """Linkedlist class."""

    def __init__(self):
        """Initialize linkedlist."""
        self.head = None

    def get(self, index: int) -> int:
        """Return item at specific index."""
        if self.head is None:
            print("Empty linked list")
            return -1
        else:
            i = 0
            curr = self.head
            while curr:
                if i == index:
                    return curr.val
                i += 1
                curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        """Insert at head of linkedlist."""
        nord = Nord(val)
        nord.next = self.head
        self.head = nord

    def addAtTail(self, val: int) -> None:
        """Insert at end of linkedlist."""
        nord = Nord(val)
        if self.head is None:
            self.head = nord
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = nord

    def addAtIndex(self, index: int, val: int) -> None:
        """Insert a nord to particular index."""
        nord = Nord(val)
        if index == 0:
            if self.head is None:
                # Empty linked list
                self.head = nord
            else:
                # Insertion at head
                nord.next = self.head
                self.head = nord
            return
        i = 0
        curr = self.head
        prev_nord = curr
        while curr:
            if i == index:
                prev_nord.next = nord
                nord.next = curr
                return
            prev_nord = curr
            curr = curr.next
            i += 1
        if i == index:
            # Insertion at tail
            prev_nord.next = nord

        print("index not found")

    def insertAfter(self, data, index):
        """Insert a nord after given node."""
        nord = Nord(data)
        if self.head is None:
            print("Empty linked list.Not inserted.")
            return -1
        else:
            i = 0
            curr = self.head
            while curr:
                if i == index:
                    nord.next = curr.next
                    curr.next = nord
                    return
                curr = curr.next
                i += 1
        print("index not found")
        return -1

    def deleteAtIndex(self, index: int) -> None:
        """Delete item at specific index."""
        if self.head is None:
            print("Empty linked list")
            return -1
        else:
            if index == 0:
                self.head = self.head.next
                return
            i = 0
            curr = self.head
            prev_nord = curr
            while curr:
                if i == index:
                    prev_nord.next = curr.next
                    curr.next = None
                    return
                prev_nord = curr
                curr = curr.next
                i += 1
        print("index not found")

    def display(self):
        """Print the linked list."""
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print("\n")


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# print(obj.addAtHead(7))
# print(obj.addAtHead(2))
# print(obj.addAtHead(1))
# print(obj.addAtTail(3))
# obj.display()
# print(obj.addAtIndex(0, 10))
# print(obj.addAtIndex(0, 20))
# print(obj.addAtIndex(1, 30))
# obj.display()
# print(obj.get(0))
# print(obj.deleteAtIndex(0))
# obj.display()
# print(obj.get(0))
# print(obj.addAtHead(6))
# print(obj.addAtTail(4))
# obj.display()
# print(obj.get(4))
# print(obj.addAtHead(4))
# print(obj.addAtIndex(5, 0))
# print(obj.addAtHead(6))
# obj.display()
