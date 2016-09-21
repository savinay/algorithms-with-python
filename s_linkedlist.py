class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        pos = 1
        val_found = False
        if self.head:
            current = self.head
            while current:
                #print current.value, pos, type(current)
                if pos == position:
                    val_found = True
                    return current
                current = current.next
                pos = pos + 1
        else:
            return None

        if val_found == False:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        pos = 1
        if self.head:
            current = self.head
            while pos != position-1:
                current = current.next
                pos = pos + 1
            new_element.next = current.next
            current.next = new_element
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            print("Cannot be inserted")
        pass


    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
    
    def removeLastElement(self):
        current = self.head
        if current: # think you could take this out (see below)
            while current.next:
                prev = current
                current = current.next
            if prev:
                prev.next = None
            else:
                self.head = None
    
    def removeFirstElement(self):
        current = self.head
        self.head = current.next
        current = None
    
    def appendAtFirst(self,value):
        current = self.head
        elem = Element(value)
        self.head = elem
        elem.next = current
                
    def lengthLinkedList(self):
        current = self.head
        # length = 0
        if current: # think you could take this out (see below)
            length = 1 # could make length a little more clean
            while current.next:
                length = length + 1
        else:
            length = 0
        return length
    
    def getLastElement(self):
        current = self.head
        if current:  # think you could take this out
            while current: # this while statement IS an if statement in a way
                current = current.next
            return current
        else:
            return None
            
    def getFirstElement(self):
        return self.head
            
        



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
# print ll

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
# print ll.get_position(3)
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)