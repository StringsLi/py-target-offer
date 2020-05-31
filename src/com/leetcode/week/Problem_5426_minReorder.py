from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = [[] for _ in range(n)]
        for c in connections:
            edges[c[0]].append((c[1], 1))
            edges[c[1]].append((c[0], 0))
        cost = 0
        stack = [0]
        visited = [False] * n
        visited[0] = True
        while len(stack) > 0:
            u = stack.pop(-1)
            for v, c in edges[u]:
                if not visited[v]:
                    visited[v] = 1
                    cost += c
                    stack.append(v)
        return cost

def minReorder2(n: int, connections: List[List[int]]) -> int:
    edges = [[] for _ in range(n)]
    for a, b in connections:
        edges[a].append([b, 1])
        edges[b].append([a, 0])

    def dfs(root, fa):
        cost = 0
        for x, c in edges[root]:
            if x == fa:
                continue
            cost += c
            cost += dfs(x, root)
        return cost
    return dfs(0, -1)

if __name__ == '__main__':
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    obj = Solution()
    print(minReorder2(n,connections))
