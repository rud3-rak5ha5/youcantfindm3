class node:
    def __init__(self, data):
        self.data = None
        self.next = None
class doubleLinkedList:
    def __init__(self):                #Password for
        self.head = None                  # server PC 
    def insert(self, data):                  #akjjy7glc_aezakm5iheso3am
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
