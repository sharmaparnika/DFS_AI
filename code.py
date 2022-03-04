graph = {
    'E':['C','G'],
    'C':['B','D'],
    'G':['H'],
    'B':[],
    'D':['H'],
    'H':[]
}

visited = []

def Depth(visited, graph, node):
  if node not in visited:
    print(node, end=" ")
    visited.append(node)
    for adj in graph[node]:
      Depth(visited, graph, adj)

print("Depth First Search")
Depth(visited, graph, 'E')
