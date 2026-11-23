class Node:
    def __init__(self):

        self.end = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:

        cur = self.root
        for letter in word:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                cur.children[letter] = Node()
                cur = cur.children[letter]

        cur.end = True

    def search(self, word: str) -> bool:
        # searching word recursively, until I hit a dot
        # then I'd launch recursive searches iteratively
        # If any return I'm home free

        def dfs(j, cur):

            if j == len(word):
                return cur.end

            if word[j] == ".":
                # launch loops for all children
                for node in cur.children.values():
                    if dfs(j + 1, node):
                        return True
                
                return False    
            else:
                if word[j] in cur.children:
                    return dfs( j + 1, cur.children[word[j]])
                else:
                    return False

        return dfs(0, self.root)



        #hi
        #**
        #*h
        #

