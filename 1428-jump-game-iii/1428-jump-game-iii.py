from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = ["N"] * (len(arr))
        queue = deque()
        if arr[start] == 0:
            return True

        def BFS(index):
            # print("queue : ", queue)
            # print(visited)
            # print(index)
            if visited[index] == "N":
                # print("in the loop")
                visited[index] = arr[index]
                # print(f"{visited},{arr}")
                if arr[index] == 0:
                    # print("should be TRUE")
                    return True
                candLeft, candRight = index - arr[index], index + arr[index]
                # print(f" candright : {candRight}, candleft : {candLeft}")
                if 0 <= candLeft <= len(arr)-1:
                    queue.append(candLeft)
                    # print(queue)
                if 0 <= candRight <= len(arr)-1:
                    queue.append(candRight)
                    # print(queue)
        BFS(start)        
        while queue:
            index = queue.popleft()
            flag = BFS(index)
            if flag:
                return True
        
        # print("BUT IS FALSE")
        return False