class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0 
        self.data = [None]*capacity

    def append(self, item):

        self.data.insert(self.current, item)
        self.current += 1
        if self.current == self.capacity:
            self.current = 0 
            
    def get(self):
        # items = []
        # for i in self.data:
        #     if i is not None:
        #         items.append(i)
        # return items 

        items = [i for i in self.data if i is not None]
        return items 


# ok, I would start with your init method. You basically need three things, capacity (which you have), 
# then a value to where you currently are initialized to 0, 
# then your storage (in your case you are calling it data) that is a list initialized to None times the capacity


# Then, in append, what do you need to do?
# 
#  You need to set the storage (or in your case data) at the index of current to the item that is being passed in as a parameter.
# 
#  You need to make sure you increment that current. 
# 
# Then if the current reaches your capacity, you need to set the current back to 0

# then, for the get method, a list comprehension might work well. You are basically iterating through your data as long as the item is not None.

