class Solution:
    def isHappy(self, n: int) -> bool:
        encountered = []

        while True:
            #split number in digits
            l = [int(d) for d in str(n)]
            print(l)
            res = 0
            for elem in l:
                res += elem**2
                print(res)
            #add their squares
            if res == 1:
                return True
            elif res in encountered:
                return False
                
            encountered.append(res)
            n = res
                #if equals to 1, return True
                #if equals to element in encountered, return False
        