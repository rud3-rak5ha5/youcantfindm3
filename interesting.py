class node:
    def __init__(self, data):
        self.data = None
        self.next = None
class doubleLinkedList:
    def __init__(self):                
        self.head = None                   
    def insert(self, data):                  
        if self.head == None:
            self.head = node(data)
            self.head.next = self.head
        else:
            new_node = node(data)
            t = self.head
            while t.next:
                t = t.next
            t.next = new_node
            new_node.next = self.head
#REMEMEBER to post it on LinkedIn: https://www.linkedin.com/in/rude-rakshas-6066b3331/
