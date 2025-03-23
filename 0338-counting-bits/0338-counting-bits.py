class Solution:
    def countBits(self, n: int) -> List[int]:
        # create result array
        res = [0] * (n + 1)
        # for number in range of n
        for i in range(0,n+1):
            # convert to bit representation
            count = 0
            bitRep = bin(i)[2:]
            # parse it for 1s
            for c in bitRep:
                if c == "1":
                    count += 1
            # add result to array
            res[i] = count
        
        return res