"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        temp=self.head
        if self.head==None:
            self.head=new_element
        while(temp.next!=None):
            temp=temp.next
        temp.next=new_element
        
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        temp=self.head
        if self.head==None:
            return None
        while(position!=1):
            temp=temp.next
            position-=1
            if temp==None:
                return None
        return temp
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        temp=self.head
        
        if position==1:
            head=new_element
            new_element.next=temp
        while(position!=1):
            temp=temp.next
            position-=1
        t=temp.next
        temp.next=new_element
        new_element.next=t
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        temp=self.head.next
        prv=self.head
        found=False
        if self.head==None:
            return None
        if prv.value==value:
            self.head=self.head.next
        while(not found):
            if temp==None:
                return "Not found"
            if temp.value==value :
                found=True
                prv.next=temp.next
            else:
                prv=prv.next
                temp=temp.next
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.value)
            temp=temp.next


# e1 = Element(1)
# e2 = Element(2)
# e3 = Element(3)

# ll = LinkedList(e1)
# ll.append(e2)
# ll.append(e3)
# # ll.delet0e(2)
# # print(ll.get_position(1))
# # print(ll.get_position(2))
# e4 = Element(4)
# ll.insert(e4,3)
# ll.delete(1)
# ll.printing()
