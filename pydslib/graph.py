class DirectedGraph:

	def __init__(self):
		'''Create an empty directed graph'''
		self.vertices = set()
		self.edges = dict()
	
	def add_vertex(self, vertex):
		'''Add vertex to graph'''
		self.__validate_vertices(vertex, expected=False)
		self.vertices.add(vertex)
		self.edges[vertex] = dict()
	
	def remove_vertex(self, vertex):
		'''Remove vertex from graph'''
		self.__validate_vertices(vertex)
		self.vertices.remove(vertex)
		for source, destinations in self.edges.items():
			if vertex in destinations:
				del destinations[vertex]
		del self.edges[vertex]
	
	def has_vertex(self, vertex):
		'''Check if graph has vertex'''
		return vertex in self.vertices
	
	def get_size(self):
		'''Get number of vertices'''
		return len(self.vertices)
	
	def iter_vertices(self):
		'''Iterate through vertices'''
		for vertex in self.vertices:
			yield vertex
	
	def add_edge(self, source, destination, edge):
		'''Add edge to graph'''
		self.__validate_vertices(source, destination)
		self.edges[source][destination] = edge
	
	def remove_edge(self, source, destination):
		'''Remove edge from graph'''
		self.__validate_vertices(source, destination)
		self.__validate_edges(source, destination)
		return self.edges[source].pop(destination)
	
	def has_edge(self, source, destination):
		'''Check if graph has edge'''
		return destination in self.edges[source]
	
	def get_edge(self, source, destination):
		'''Get edge between two vertices'''
		self.__validate_edges(source, destination)
		return self.edges[source][destination]
	
	def get_degree(self, source):
		'''Get number of neighbours'''
		self.__validate_vertices(source)
		return len(self.edges[source])
	
	def iter_neighbours(self, source):
		'''Iterate through neighbours'''
		self.__validate_vertices(source)
		for destination, edge in self.edges[source].items():
			yield destination, edge
	
	def dfs(self, source):
		'''Perform a depth-first search'''
		return self.__dfs(source, set())
	
	def __dfs(self, source, visited):
		self.__validate_vertices(source)
		dfs_list = []
		if source not in visited:
			visited.add(source)
			dfs_list.append(source)
			for neighbour in self.edges[source]:
				dfs_list += self.__dfs(neighbour, visited)
		return dfs_list
	
	def bfs(self, source):
		'''Perform a breadth-first search'''
		self.__validate_vertices(source)
		from collections import deque
		bfs_list = []
		bfs_deque = deque()
		visited = set()
		if source not in visited:
			bfs_deque.append(source)
			visited.add(source)
			while len(bfs_deque) > 0:
				vertex = bfs_deque.popleft()
				bfs_list.append(vertex)
				for neighbour in self.edges[vertex]:
					if neighbour not in visited:
						bfs_deque.append(neighbour)
						visited.add(neighbour)
		return bfs_list
	
	def __validate_vertices(self, *vertices, expected=True):
		for vertex in vertices:
			if self.has_vertex(vertex) != expected:
				raise Exception("Vertex '{}' is {} in graph".format(
								vertex, "not" if expected else "already"))
	
	def __validate_edges(self, source, destination, *edges, expected=True):
		if self.has_edge(source, destination) != expected:
				raise Exception("Edge between {} and {} is {} in graph".format(
								source, destination, "not" if expected else "already"))
		for edge in edges:
			if (self.get_edge(source, destination) == edge) != expected:
				raise Exception("Edge '{}' between {} and {} is {} in graph".format(
								source, destination, edge, "not" if expected else "already"))

class UndirectedGraph(DirectedGraph):

	def add_edge(self, source, destination, edge):
		super().add_edge(source, destination, edge)
		self.edges[destination][source] = edge

	def remove_edge(self, source, destination):
		edge = super().remove_edge(source, destination)
		del self.edges[destination][source]
		return edge

class GraphFactory:
	
	@staticmethod
	def get_empty_graph(size=10, directed=True):
		g = DirectedGraph() if directed else UndirectedGraph()
		for v in range(size):
			g.add_vertex(v)
		return g
	
	@staticmethod
	def get_full_graph(size=10, directed=True):
		g = GraphFactory.get_empty_graph(size, directed)
		for v in range(size):
			for w in range(size):
				g.add_edge(v, w, v*w)
		return g