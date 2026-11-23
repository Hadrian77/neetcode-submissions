class LRUCache:

    def __init__(self, capacity: int):
        self.old = Node()
        self.recent = Node()

        self.recent.next = self.old
        self.old.prev = self.recent

        self.capacity = capacity
        self.cache = {}


    def get(self, key: int) -> int:

        if key in self.cache:
            self.update(self.cache[key])
            return self.cache[key].val
        
        else: 
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.update(self.cache[key])
            self.cache[key].val = value

        else:
            new = Node()
            new.key = key
            new.val = value

            self.cache[key] = new
            self.add(new)

            if len(self.cache) > self.capacity:
                del self.cache[self.removeOldest().key]
    

    def add(self,new):

        self.recent.next.prev = new
        new.prev = self.recent

        new.next = self.recent.next
        self.recent.next = new



    def removeOldest(self):

        oldest = self.old.prev
        self.old.prev = oldest.prev
        oldest.prev.next = self.old
        
        return oldest
    
    def update(self,node):

        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.recent
        node.next = self.recent.next
        self.recent.next.prev = node

        self.recent.next = node

class Node:

    def __init__(self):
        self.key = None
        self.val = None
        self.next = None
        self.prev = None
        
