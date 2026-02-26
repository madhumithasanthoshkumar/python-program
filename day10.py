# class node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# n1 = node(1)
# n2 = node(2)
# n3 = node(3)
# n1.next = n2
# n2.next = n3
# print(n1.value)
# print(n1.next.value)
# print(n1.next.next.value)
class node:
    def __init__(self, value):
        self.value = value
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        newNode = node(data)
        newNode.next = self.head
        self.head = newNode
    def insert_end(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode   
    def display(self):
        temp = self.head   
        while temp:
            print(temp.value, end="->")  
            temp = temp.next
        print("None")



li = linkedlist()
li.insert_begin(10)
li.insert_begin(5)
li.insert_begin(20)
li.insert_begin(30)
li.insert_end(50)

li.display()