class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        temp = self.queue[0]
        del self.queue[0]
        return temp
    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue("mon")
q.enqueue("tues")
print(q.size())
print(q.dequeue())
print(q.size())


