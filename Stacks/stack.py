class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         if self.isEmpty():
             return None
         temp = self.items[-1]
         del self.items[-1]
         return temp

     def peek(self):
         return self.items[-1]

     def size(self):
         return len(self.items)
s = Stack()
s.push('hello')
s.push('true')
print(s.pop())
