class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()

        def dfs(node, parent):
            # check if node in seen set
            if node in seen:
                return False
            # add node to seen set
            seen.add(node)

            # explore neighbours (if they are not the parent)
            for edge in edges:
                if edge[0] == node and edge[1] != parent:
                    if not dfs(edge[1], node):
                        return False
                elif edge[1] == node and edge[0] != parent:
                    if not dfs(edge[0], node):
                        return False
            return True

        # return true if seen set has length n
        if not dfs(0, -1):
            return False

        
        
        return len(seen) == n