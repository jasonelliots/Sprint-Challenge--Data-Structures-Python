class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [i for i in range(capacity)]

    def append(self, item):
        self.data.pop(0)
        self.data.append(item)
            
    def get(self):
        return self.data

# class RingBuffer:

#     def __init__(self,size_max):
#         self.max = size_max
#         self.data = []

#     def append(self,x):
#         self.data.append(x)
#         if len(self.data) == self.max:
#             self.data.pop(0)

#     def get(self):
#         return self.data