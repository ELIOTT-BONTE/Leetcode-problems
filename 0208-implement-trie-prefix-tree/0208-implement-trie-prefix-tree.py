class Node:
    def __init__(self):
        self.is_end = False
        self.neighbours = {}

class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if not char in node.neighbours:
                node.neighbours[char] = Node()
            node = node.neighbours[char]
        node.is_end = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if not char in node.neighbours:
                return False
            node = node.neighbours[char]
        return node.is_end
        


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if not char in node.neighbours:
                return False
            node = node.neighbours[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)