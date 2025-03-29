from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graph = defaultdict(list)
        inc = [0]*numCourses
        processed = 0 #count processed nodes

        for dest, src in prerequisites:
            graph[src].append(dest)
            inc[dest] += 1

        process = deque([i for i in range(numCourses) if inc[i] == 0]) #add to queue all nodes that have 0 incoming edges

        # process nodes

        # for each node
        # increase count of nodes processed
        while process:
            node = process.popleft()
            processed +=1
            # reduces inc of its neighbors by one
            for neighbor in graph[node]:
                inc[neighbor] -=1
                if inc[neighbor] == 0:
                    process.append(neighbor)
            # if neighbor has 0 inc, add it to queue
        return processed == numCourses