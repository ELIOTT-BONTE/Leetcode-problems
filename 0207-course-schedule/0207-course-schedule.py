from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make the graph
        graph = defaultdict(list)
        # make the incomingEdges array
        incomingEdges = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            incomingEdges[dest] += 1

        queue = deque([i for i in range(numCourses) if incomingEdges[i] == 0])
        
        deleted = 0
        #count of nodes deleted

        while queue:
            node = queue.popleft()
            deleted += 1
            for neighbour in graph[node]:
                incomingEdges[neighbour] -= 1
                if incomingEdges[neighbour] == 0:
                    queue.append(neighbour)
        
        return deleted == numCourses
        #delete node if it has 0 incoming edges
        #decrease incoming edges of its neighbours by 1

        #return deletedNodes == numCourses

