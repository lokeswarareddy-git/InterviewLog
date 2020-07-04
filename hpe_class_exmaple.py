# Stack Implimentation

class Stack(object):
    def __init__(self):
       self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
s.push(2)
s.push(4)
s.push("Three")
print(s.peek())
print(s.size())
print(s.isEmpty())


 
           
    




