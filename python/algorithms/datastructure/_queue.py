class Queue:
    arr: list

    def __init__(self) -> None:
        self.arr = []
    
    def enqueue(self, num):
        self.arr.append(num)
    
    def dequeue(self):
        if self.size() == 0:
            return None

        return self.arr.pop(0)

    def peek(self):
        return self.arr[-1]

    def size(self):
        return len(self.arr)
    
    def display(self):
        print(self.arr)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
q.dequeue()
print("After removing an element")
q.display()
