"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)
        print("The elements are:",self.storage)

    def peek(self):
        return self.storage
       
    def dequeue(self):

        self.storage.pop(0)
        print("The elements are popped",self.storage)


q = Queue(1)
# print(q)
q.enqueue(2)
# print(q)
q.enqueue(3)
# print(q)
q.dequeue()
# print(q)
