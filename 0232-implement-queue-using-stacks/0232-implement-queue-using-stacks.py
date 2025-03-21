class MyQueue(object):

    def __init__(self):
        self.one = []
        self.two = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.one.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        while self.one:
            self.two.append(self.one.pop())
        r = self.two.pop()
        while self.two:
            self.one.append(self.two.pop())
        return r
        

    def peek(self):
        """
        :rtype: int
        """
        while self.one:
            self.two.append(self.one.pop())
        r = self.two[-1]
        while self.two:
            self.one.append(self.two.pop())
        return r
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.one
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()