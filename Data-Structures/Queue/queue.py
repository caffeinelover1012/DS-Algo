class Queue:
    def __init__(self) -> None:
        self.q = []
    
    def enqueue(self,element):
        print("Enquining", element)
        self.q.append(element)

    def dequeue(self):
        elem = self.q.pop(0)
        print("Dequeued ", elem)
        return elem

    def print(self):
        print(self.q)

    def empty(self):
        return len(self.q)==0
     
    def front(self):    
        return self.q[0]

    def back(self):
        return self.q[-1]
    
    def size(self):
        return len(self.q)

q = Queue()
print("Is Queue empty: ", q.empty())
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print()
q.dequeue()
q.print()
