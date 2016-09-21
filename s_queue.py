from s_linkedlist import LinkedList, Element

class Queue:
    def __init__(self,value):
        elem = Element(value)
        self.ll = LinkedList(elem)
    def isEmpty(self):
        return self.ll.lengthLinkedList() == 0
    def enqueue(self, value):
        self.ll.appendAtFirst(value)
    def dequeue(self):
        self.ll.removeLastElement()
    def size(self):
        return self.ll.lengthLinkedList()