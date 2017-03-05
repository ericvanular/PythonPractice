#kruskals algorithm


def kruskals(edges, num_edges, start_vertex):
    mst_cost = 0
    num_visited_edges = 0
    
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    
    visited_vertices = set()
    visited_vertices.add(start_vertex)
    
    while len(visited_vertices) != num_edges:    
        print visited_vertices
        for edge1, edge2, cost in sorted_edges:
            if edge1 in visited_vertices and edge2 not in visited_vertices:
                #print "edge 1 " + str(edge1) + " edge 2 " + str(edge2)
                visited_vertices.add(edge2)
                mst_cost += cost
                break
            elif edge1 not in visited_vertices and edge2 in visited_vertices:
                visited_vertices.add(edge1)
                mst_cost += cost
                break
                
    return mst_cost              
        
def get_num_edges(connections):
    
    all_connections = [x[0] for x in connections]
    all_connections.extend([x[1] for x in connections])
    
    all_connections = sorted(all_connections)
    
    num_edges = 1
    
    for idx,edge in enumerate(all_connections):
        if idx != 0:
            if edge != all_connections[idx - 1]:
                num_edges += 1
    
    return num_edges
          


graph_str = '''5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1'''


graph = graph_str.split("\n")
start_node = graph[-1]
graph = graph[1:-1]
graph_vertices = []
for edge in graph:
    edge = edge.split()
    edge = [int(i) for i in edge]
    graph_vertices.append(edge)


num_edges = get_num_edges(graph_vertices)
print kruskals(graph_vertices, num_edges, 1)
