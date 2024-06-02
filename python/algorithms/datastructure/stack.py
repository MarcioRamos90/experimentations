class Stack:
    arr: list
    size: int

    def __init__(self, size) -> None:
        self.size = size
        self.arr = []
    
    def push(self, num):
        self.arr.append(num)
    
    def pop(self):
        if self.size() == 0:
            raise Exception("could not do it")

        return self.arr.pop()
    
    def size(self):
        return len(self.arr)
    
    def get(self):
        return self.arr[-1]