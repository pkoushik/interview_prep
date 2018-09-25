class Heap:
    def __init__(self):
        self.size = 0
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.size = self.size + 1
        print(self.heap)
        i = self.size - 1
        while val < self.heap[(i-1)//2] and i >= 0:
            temp = self.heap[i]
            self.heap[i] = self.heap[(i-1)//2]
            self.heap[(i-1)//2] = temp
            i = ( i - 1 ) // 2

    def getMin(self):
        if self.size == 0:
            return None
        return self.heap[0]
 
    def removeMin(self):
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.size = self.size - 1
        if self.size > 0:
            self.sink(0)

    def sink(self, index):
        leftChildIndex = (2 * index) + 1
        rightChildIndex = (2 * index) + 2
        if rightChildIndex >= self.size:
            if leftChildIndex >= heapSize:
                return
            else:
                minIndex = leftChildIndex
        else:
            if self.heap[leftChildIndex] <= self.heap[rightChildIndex]:
                minIndex = leftChildIndex
            else:
                minIndex = rightChildIndex

        if self.heap[index] > self.heap[minIndex]:
            tmp = self.heap[minIndex]
            self.heap[minIndex] = self.heap[nodeIndex]
            self.heap[nodeIndex] = tmp
            self.sink(minIndex)
    

    def printHeap(self):
        print(self.heap)

h = Heap()
h.insert(10)
h.insert(6)
h.insert(20)
h.insert(5)
h.insert(16)
h.insert(17)
h.insert(13)
h.insert(2)
# h.removeMin()
h.printHeap()
