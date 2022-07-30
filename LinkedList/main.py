class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        print(self.head)
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            self.insert_at_beginning(self, data)

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def length_of_ll(self):
        if self.head == None:
            # print("Length Is 0")
            return 0
        count = 1
        itr = self.head
        while itr.next:
            count += 1
            itr = itr.next
        # print(f"Lenght is {count}")
        return count

    def insert_at_index(self, data, index):
        if self.length_of_ll() < index:
            return print(f"Cannot insert at index {index}, because length_of_ll is {self.length_of_ll()}")

        count = 1
        itr = self.head
        while count < index:
            count += 1
            itr = itr.next
        itr.next = Node(data, itr.next)
        return self.print()

    def remove_element_at_index(self, index):
        if self.length_of_ll() < index:
            return print(f"Cannot Remove at index {index}, because length_of_ll is {self.length_of_ll()}")

        count = 0
        itr = self.head
        while count < index - 1:
            count += 1
            itr = itr.next
        itr.next = itr.next.next

        return self.print()

    def insert_multiple_values(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next

        for x in data:
            itr.next = Node(x, None)
            itr = itr.next

        return self.print()

    def insert_multiple_values_at_start_index(self, data, index):
        if self.length_of_ll() < index:
            return print(f"Cannot Insert at index {index}, because length_of_ll is {self.length_of_ll()}")
        itr = self.head
        count = 0
        while count < index - 1:
            itr = itr.next
            count += 1
        for x in data:
            itr.next = Node(x, itr.next)
            itr = itr.next
        return self.print()

    def remove_value_from_ll(self, data):

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
            else:
                itr = itr.next

        return self.print()

    def print(self):
        if self.head == None:
            print("List is Empty ")
            return

        itr = self.head
        listStr = ""
        while itr:
            if itr.next:
                listStr += str(itr.data) + '-->'
            else:
                listStr += str(itr.data)
            itr = itr.next

        print(listStr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(5)
    ll.insert_at_end(30)
    print(ll.length_of_ll())
    ll.print()
    ll.insert_multiple_values([1,2,3])
    ll.insert_multiple_values_at_start_index([1, 2, 2, 3], 2)
    ll.insert_at_index(45, 3)
    ll.remove_element_at_index(2)
    ll.remove_value_from_ll(2)
