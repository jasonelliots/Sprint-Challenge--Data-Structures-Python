class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0 
        self.data = [None]*capacity

    def append(self, item):

        if self.current == self.capacity:
            self.current = 0 
        self.data[self.current] = item
        self.current += 1
       
            
    def get(self):

        items = [i for i in self.data if i is not None]
        return items 

