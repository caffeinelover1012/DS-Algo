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

    def add_at_idx(self,idx,node=None):
        if idx:
            if not self.head:
                self.head = node
                return
            count = 0
            temp = self.head   

    def reverse(self):
        if not self.head:
            return 
        else:
            prev = None
            curr = self.head
            while curr!=None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp                
            self.head = prev

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
print("Reversing Linked List in place")
ll.reverse()
ll.print()