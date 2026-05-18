class Node:

    def __init__(self,word=""):
        self.children = {}
        self.wd = word


class PrefixTree:

    def __init__(self):
        self.head = Node()
        

    def insert(self, word: str) -> None:
        cur = self.head
        wd = ""
        for i in word:
            wd += i
            if i not in cur.children:
                cur.children[i] = Node()

            cur = cur.children[i]
        cur.wd = wd
        
            


    def search(self, word: str) -> bool:
        cur = self.head
        for i in word:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return cur.wd == word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for i in prefix:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return True
        