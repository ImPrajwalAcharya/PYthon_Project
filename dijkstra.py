import time
from variables import *
def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        for childNode, weight in graph[minNode].items():
            egdes=minNode+childNode
            l= future_time_calc(traffic_lights_data[egdes][0], traffic_lights_data[egdes][1], traffic_lights_data[egdes][2],weight+shortest_distance[minNode])
            print(egdes+":"+str(l)+"-------->"+str(weight))
            if l[1]=='Green':
                if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                        shortest_distance[childNode] = weight + shortest_distance[minNode]
                        predecessor[childNode] = minNode
            else:
                if weight + shortest_distance[minNode]+traffic_lights_data[egdes][2]-l[0] < shortest_distance[childNode]:
                        shortest_distance[childNode] = weight + shortest_distance[minNode]+traffic_lights_data[egdes][2]-l[0]
                        predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest time to travel from ' +start+' to '+goal+' is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
# print(time_to_reach_to_lights)
# print(future_light_condition)
# print(traffic_lights_data_value1)
# print(traffic_lights_data_value2)
dijkstra(graph, 'a', 'b')
