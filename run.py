# Search methods

import search

ab = search.GPSProblem('L', 'R', search.romania)


print("anchura")
print(search.breadth_first_graph_search(ab).path())
print("profundidad")
print(search.depth_first_graph_search(ab).path())
print("ramificación y acotación")
print(search.breadth_first_graph_search_2(ab).path())
print("ramificación y acotación con subestimación")
print(search.breadth_first_graph_search_h(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
