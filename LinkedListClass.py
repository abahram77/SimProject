#This class indicates one node and the previous and the next node
class Node:
    def __init__(self, val):
        self.val = val
        self.next_node = None
        self.pre_node = None

    def __str__(self):
        return str(self.pre_node) + " " + str(self.val.number) + " " + str(self.pre_node)


#This class is a list of nodes and their functions
class LinkedList:
    def __init__(self):
        self.start_node = None
        self.last_node = None
        self.length = 0

    #With this function we can add a node to our list
    def insert_at_start(self, data):
        self.length += 1
        new_node = Node(data)
        if self.start_node is not None:
            new_node.next_node = self.start_node
            self.start_node.pre_node = new_node
        else:
            self.last_node = new_node
        self.start_node = new_node

    #With this function we can read and pop the last node from our list
    def pop_last(self):
        node = self.last_node
        if node is not None:
            self.length -= 1
            if node.pre_node is None:
                self.start_node = None
            else:
                node.pre_node.next_node = None
            self.last_node = node.pre_node
            return node.val

    def filter(self, func):
        node = self.start_node
        removed_values = []
        while node is not None:
            if not func(node.val):
                removed_values += [node.val]
                if node.pre_node is None:
                    self.start_node = node.next_node
                else:
                    node.pre_node.next_node = node.next_node
                if node.next_node is None:
                    self.last_node = node.pre_node
                else:
                    node.next_node.pre_node = node.pre_node
            node = node.next_node
        self.length -= len(removed_values)
        return removed_values

    #This function shows us the sequence of node values in linked list
    def __str__(self):
        x = "linked list ["
        n = self.start_node
        while n is not None:
            x += str(n.val) + ", "
            n = n.next_node
        return x + " ]"

