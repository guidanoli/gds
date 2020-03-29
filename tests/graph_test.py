from pydslib import graph

def test_empty_graph():
	g = graph.DirectedGraph()
	assert len(g) == 0
	for v in g.iter_vertices():
		assert False

def test_add_and_remove_vertex():
	g = graph.DirectedGraph()
	g.add_vertex(0)
	assert len(g) == 1
	for v in g.iter_vertices():
		assert v == 0
	assert g.has_vertex(0)
	assert g.get_degree(0, i=True, o=True) == 0
	for vertex in g.iter_neighbours(0, i=True, o=True):
		assert False
	g.remove_vertex(0)
	assert len(g) == 0
	for v in g.iter_vertices():
		assert False
	assert not g.has_vertex(0)

def test_add_error():
	g = graph.DirectedGraph()
	g.add_vertex(0)
	try:
		g.add_vertex(0)
	except:
		return
	assert False

def test_remove_error():
	g = graph.DirectedGraph()
	try:
		g.remove_vertex(0)
	except:	
		return
	assert False

def test_add_remove_edge():
	g = graph.DirectedGraph()
	g.add_vertex(0)
	g.add_vertex(1)
	g.add_edge(0,1,2)
	assert g.has_edge(0,1)
	assert g.get_edge(0,1) == 2
	assert g.get_degree(0,i=False,o=False) == 0
	assert g.get_degree(0,i=False,o=True) == 1
	assert g.get_degree(0,i=True,o=False) == 0
	assert g.get_degree(0,i=True,o=True) == 1
	assert g.get_degree(1,i=False,o=False) == 0
	assert g.get_degree(1,i=False,o=True) == 0
	assert g.get_degree(1,i=True,o=False) == 1
	assert g.get_degree(1,i=True,o=True) == 1
	for info in g.iter_neighbours(0, i=True, o=True):
		assert info == (1, 2, 1)
	for info in g.iter_neighbours(1, i=True, o=True):
		assert info == (0, 2, -1)
	assert g.remove_edge(0,1) == 2
	assert g.get_degree(0, i=True, o=True) == 0
	assert g.get_degree(1, i=True, o=True) == 0
	for vertex in g.iter_neighbours(0, i=True, o=True):
		assert False
	for vertex in g.iter_neighbours(1, i=True, o=True):
		assert False

def test_dfs():
	gk10 = graph.GraphFactory.get_full_graph(10)
	visited = [vertex for vertex in gk10.dfs(0)]
	assert len(visited) == 10
	for i in range(10):
		assert i in visited

def test_bfs():
	gk10 = graph.GraphFactory.get_full_graph(10)
	visited = [vertex for vertex in gk10.bfs(0)]
	assert len(visited) == 10
	for i in range(10):
		assert i in visited