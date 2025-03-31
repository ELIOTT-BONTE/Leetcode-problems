class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        # init the historySize and currentPage counters
        self.histSize, self.curr = 0, 0
        self.hist = [homepage]
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        
        self.curr += 1
        self.histSize = self.curr
        if  self.curr > len(self.hist)-1:
            self.hist.append(url)
        else:
            self.hist[self.curr] = url
        
        
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps <= self.curr:
            self.curr -= steps
        else:
            self.curr = 0 # avoids out of boundary
        return self.hist[self.curr]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps + self.curr <= self.histSize:
            self.curr += steps
        else:
            self.curr = self.histSize
        return self.hist[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)