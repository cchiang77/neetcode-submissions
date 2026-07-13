class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def explore(graph, current, visited):
            if current in visited:
                return False
            visited.add(current)
            for neighbor in graph[current]:
                explore(graph, neighbor, visited)
            return True

        def build_graph(n, edges):
            graph = {i: [] for i in range(n)}
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)
            return graph

        graph = build_graph(n, edges)
        count = 0
        visited = set()

        for node in range(n):
            if explore(graph, node, visited) == True:
                count += 1
        return count