class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class BaseList:
    def __init__(self):
        self.head = None

    def push(self):
        pass

    def print_nodes(self):
        pass

    def __len__(self):
        c = 0
        tmp = self.head

        if self.head == None:
            return 0
        else:
            while tmp:
                c+=1
                tmp = tmp.next

            return c

class LinkedList(BaseList):
    def push(self, data):
        '''
        Recive the data for the new node. Create the node and append it to the head of the list.
        '''
        # create the new node
        node = Node(data)

        if self.head is not None:
            node.next = self.head
        self.head = node

    def print_nodes(self):
        tmp = self.head
        if self.head is not None:
            while tmp:
                print(tmp.data)
                tmp = tmp.next


class DoublelinkedList(LinkedList):
    def push(self, data):
        node = Node(data)

        if self.head is not None:
           tmp = self.head
           node.next = tmp
           while  True:
               if tmp.next == self.head:
                    self.head = node
                    tmp.next = node
                    break
               tmp = tmp.next
        else:
            self.head = node
            self.head.next = node
    def print_nodes(self):
        tmp = self.head
        while True:
            print(tmp.data)
            tmp = tmp.next
            if tmp == self.head:
                break

    def __len__(self):
        tmp = self.head
        c = 0

        while True:
            c +=1
            tmp = tmp.next
            if tmp == self.head:
                break

        return c
