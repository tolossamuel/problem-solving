class GraphOperations:
    def __init__(self, num_vertices):
        self.vertices_dict = {}
        for i in range(1, num_vertices + 1):
            self.vertices_dict[i] = []

    def add_edge(self, u, v):
        self.vertices_dict[u].append(v)
        self.vertices_dict[v].append(u)

    def get_adjacent(self, u):
        return self.vertices_dict[u]

def main():
    num_vertices = int(input())
    num_operations = int(input())
    graph_ops = GraphOperations(num_vertices)
    
    for _ in range(num_operations):
        operation = input().split()
        if operation[0] == "1":
            u, v = map(int, operation[1:])
            graph_ops.add_edge(u, v)
        elif operation[0] == "2":
            u = int(operation[1])
            adjacent_vertices = graph_ops.get_adjacent(u)
            print(" ".join(map(str, adjacent_vertices)))

if __name__ == "__main__":
    main()
