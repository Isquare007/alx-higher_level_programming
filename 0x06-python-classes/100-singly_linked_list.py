#!usr/bin/python3
"""Creates a node for singly list link"""
class Node


def __init__(self, data=0, next_node=0):
    self.__data = node
    self.__next_node = next_node


@property
def data(self):
    return (self.__data)


@data.setter
def data(self, value):
    if not isinstance(value, int):
        raise TypeError("data must be an integer")
    self.__data = value


@property
def next_node(self):
    return (self.__next_node)


@next_node.setter
def next_node(self, value):
    if not isinstance(value, node) and
    value is not None:
        raise TypeError("next_node must be a Node object")
    self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initialize a new SignlyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the Singly Linked List.
        value(Node): The new node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self._head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print representation of the SinglyLinkedList."""
        value = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
            return ('\n'.join(values))
