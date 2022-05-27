class Node:
   def __init__(self, val=None):
      self.val = val
      self.next  = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def print(self):
        temp = self.head
        if not temp:
            print("Empty List!")
            return
        while(temp.next!=None):
            print(temp.val,end=" -> ")
            temp=temp.next
        print(temp.val)

    def add_to_front(self,node = None):
        if node:
            node.next = self.head
            self.head = node
        else:
            print("Pass the node you want to add.")
            return

    def add_to_end(self,node=None):
        if node:
            temp = self.head
            if not temp:
                self.head = node
            else:
                while(temp.next!=None):
                    temp=temp.next
                temp.next = node
                print(f"Added {node.val} to the end")
        else:
            print("Pass the node you want to add.")
            return

n3 = Node(3)
n2 = Node(2)
n2.next = n3
n1 = Node(1)
n1.next = n2

ll = LinkedList(n1)
ll.print()
ll.add_to_end(Node(13))
ll.add_to_front(Node(0))
ll.print()