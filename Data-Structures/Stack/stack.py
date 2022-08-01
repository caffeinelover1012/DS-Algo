class Stack:
    def __init__(self):
        self.stack = []
    
    def add(self,elem):
        print("Adding Element")
        self.stack.append(elem)
    
    def pop(self):
        toBeReturned = self.stack.pop()
        return toBeReturned

    def print(self):
        print("Elements in Stack:")
        print(self.stack)

    def size(self):
        return len(self.stack)

st = Stack()
st.add(3)
st.add(5)
st.add(7)
st.add(6)
st.print()
popped = st.pop()        
print(popped, " was popped")
st.print()
