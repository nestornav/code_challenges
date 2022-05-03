class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        '''
        Recive the data for the new node. Create the node and append it to the head of the list.
        '''
        # create the new node
        node = Node(data)

        if self.head != None:
            node.next = self.head
        self.head = node

    def print_nodes(self):
        tmp = self.head
        if self.head is not None:
            while tmp:
                print(tmp.data)
                tmp = tmp.next

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

class DoublelinkedList(LinkedList):
    def push(self, data):
        pass
    def print_nodes(self):
        pass

    def __len__(self):
        pass
