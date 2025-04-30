from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        code = "0000"
        count = 0
        visited = set(deadends)

        if "0000" in visited:
            return -1
        elif target == "0000":
            return 0


        queue = deque([(code, count)])
        while queue:
            code,count = queue.popleft()

            for i in range(4):
                digit = code[i]
                for delta in [-1,1]:
                    new_digit = (int(digit) + delta) % 10
                    new_code = code[0:i] + str(new_digit) + code[i+1:5]
                    if new_code == target:
                        return count+1
                    if new_code not in visited:
                        visited.add(new_code)
                        queue.append((new_code, count+1))

        return -1
                    
                    