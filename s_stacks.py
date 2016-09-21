from s_linkedlist import LinkedList, Element

class Stack:
    def __init__(self):
        self.stackItems = []
    def push(self, val):
        self.stackItems.append(val)
    def pop(self):
        self.stackItems.pop()
    def lenStack(self):
        return len(self.stackItems)
    def isEmpty(self):
        return True if len(self.stackItems) == 0 else False
    def peek(self):
        return self.stackItems[len(self.stackItems) - 1]

class StackLinkedList:
    def __init__(self,value):
        elem = Element(value)
        self.ll = LinkedList(elem)
    def push(self, value):
        # elem = Element(value)
        self.ll.appendAtFirst(value)
    def pop(self):
        self.ll.removeFirstElement()
    def lenStack(self):
        return self.ll.lengthLinkedList()
    def isEmpty(self):
        return self.ll.lengthLinkedList() == 0
    def peek(self):
        return self.ll.getFirstElement().value
        
myStack = StackLinkedList(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.pop()
print(myStack.peek())