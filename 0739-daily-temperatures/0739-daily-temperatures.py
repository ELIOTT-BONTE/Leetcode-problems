class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                #register difference in index in res
                res[stack[-1][0]] = i-stack[-1][0] #store difference in indices as distance between days
                #then pop
                stack.pop()
            
            stack.append([i, temp])

        return res