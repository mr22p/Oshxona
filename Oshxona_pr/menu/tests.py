from collections import deque

graph = {
'A': ['B','C'],
'B': ['D','E'],
'C': ['F'],
'D': [],
'E': [],
'F': []
}

visited = []
queue = deque(['A'])

while queue:
    node = queue.popleft()
    if node not in visited:
        print(node)
        visited.append(node)
        queue.extend(graph[node])


graph = {
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node)
        visited.add(node)
        for n in graph[node]:
            dfs(n)

dfs('A')        