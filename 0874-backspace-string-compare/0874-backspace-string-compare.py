class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            skip = 0 #keep track of how many characters when need to skip
            for x in reversed(s):
                if x == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x #makes this function a generator
        
        return all(x == y for x,y in itertools.zip_longest(helper(s),helper(t))) #compare characters being generated