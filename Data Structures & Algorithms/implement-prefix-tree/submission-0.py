class PrefixTree:

    def __init__(self):
        #Create a root node, and even possibly define what a node is here
        #One of my properties should define a pointer to the root. I think the node should be a hashmap
        #O(1) time complexity
        
        self.root = {}


    def insert(self, word: str) -> None:
        ##Check for existence first, if its not there make a new node in  hashmap
        # O(n) time complexity where ne is the letters in the string

        current = self.root

        for x in word:
            if x in current:
                current = current[x]
            else:
                current[x] = {}
                current = current[x]
        
        current[1] = 1



    def search(self, word: str) -> bool:
        #Search recursively, going down levels, if you cant find a level, return false
        # O(n) time complexity where ne is the letters in the string
        
        current = self.root

        for x in word:
            if x in current:
                current = current[x]
            else:
                return False

        if 1 not in current:
            return False
        
        return True

    def startsWith(self, prefix: str) -> bool:
        #same as search, might even use the same functionality here, like just calling search
        # O(n) time complexity where ne is the letters in the string

        current = self.root

        for x in prefix:
            if x in current:
                current = current[x]
            else:
                return False

        return True
