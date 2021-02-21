#!/usr/bin/env python3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data, prev_node=None, position=None):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return True

        if prev_node:
            temp = prev_node.next
            prev_node.next = new_node
            new_node.next = temp
            return True

        if position:
            last = self.find_index(index=position)
            if last == self.head:
                last.next = self.head
                self.head = last
                return True
            return self.add(data, prev_node=last)

        last = self.find_index()
        last.next = new_node
        return True

    def find_index(self, index=None):
        last = self.head
        counter = 0
        while (last.next):
            last = last.next
            if counter == index:
                break
            counter += 1
        return last

    def deleteNode(self, data, prev_node=None):
        if prev_node:
            temp = prev_node.next
            next_node = temp.next
            prev_node = next_node
            return True
        target_node = self.find_data(data)
        if target_node:
            return self.deleteNode(prev_node=target_node)
        return False

    def find_data(self, data):
        last = self.head
        prev_node = None
        while (last.next):
            if last.data == data:
                break
            prev_node = last
            last = last.next
        return prev_node