#implementation of dijkstas algorithm

def dijkstras(connections, num_nodes, start_node):
    queued_nodes = set()
    queued_nodes.add(1)
    visited_nodes = set()
    distances = dict()
    for vertex in range(1, num_nodes + 1):
        distances[vertex] = float("inf")
    distances[1] = 0
    
    current_node = get_min_dist_node(queued_nodes, distances)
    
    while current_node != -1 and len(queued_nodes) != 0:
        adjacent_nodes = get_adjacent_nodes(current_node, connections)
        for adjacent_node in adjacent_nodes:
            if distances[current_node] + 6 < distances[adjacent_node]:
                distances[adjacent_node] = distances[current_node] + 6
            if adjacent_node not in visited_nodes:
                queued_nodes.add(adjacent_node)
            queued_nodes = queued_nodes - set([current_node])
            visited_nodes.add(current_node)
            
        current_node = get_min_dist_node(queued_nodes, distances)
        
    return distances
        
    
def get_min_dist_node(queued_nodes, distances):
    min_dist = float("inf")
    min_dist_node = -1
    for node in queued_nodes:
        if distances[node] < min_dist:
            min_dist = distances[node]
            min_dist_node = node
            
    return min_dist_node
    
def get_adjacent_nodes(start_node, connections):
    adjacent_nodes = set()
    for vertex1, vertex2 in connections:
        if vertex1 == start_node:
            adjacent_nodes.add(vertex2)
        elif vertex2 == start_node:
            adjacent_nodes.add(vertex1)
            
    return adjacent_nodes
    
def get_nodes(graph):
    nodes = []
    graph_copy = graph.split("\n")[1:-1]
    for edge in graph_copy:
        nodes.append([int(i) for i in edge.split()])
        
    return nodes

graph = '''4 2
1 2
1 3
1 4
1'''

num_nodes = 4
num_edges = 2
start_node = 1


connections = get_nodes(graph)
#get_adjacent_nodes(1, connections)
print dijkstras(connections, num_nodes, start_node)