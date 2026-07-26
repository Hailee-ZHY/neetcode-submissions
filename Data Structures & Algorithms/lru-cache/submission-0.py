class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key: int, value: node
        self.cap = capacity
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    # move to the Most Recent
    def move(self, node):
        temp = self.mru.prev
        temp.next = self.mru.prev = node
        node.prev = temp
        node.next = self.mru

    # remove
    def remove(self, node):
         prev = node.prev 
         next = node.next
         prev.next = next
         next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove
            self.remove(self.cache[key])
            # move
            self.move(self.cache[key])
            return self.cache[key].value
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.move(self.cache[key])

        while len(self.cache) > self.cap:
            temp = self.lru.next
            self.remove(self.lru.next)
            del self.cache[temp.key]
        


    # 1,10 -> 2,20 -> 3,30
    # remove the least recently used
    

  
    