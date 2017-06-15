### create vertex
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = 'white'

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connection(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


# create graph framework for adding connections between vertices
class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())



## Implement chess logic to add connections to vertices
def knights_graph(board_size):
    knight_graph = Graph()

    for row in range(board_size):
        for col in range(board_size):
            node_id = position_to_node_id(row, col, board_size)
            new_positions = gen_legal_moves(row, col, board_size)
            for e in new_positions:
                n_id = position_to_node_id(e[0], e[1], board_size)
                print (row, col, n_id)
                knight_graph.add_edge(node_id, n_id)

    return knight_graph

def position_to_node_id(row, column, board_size):
    return (row * board_size) + column

def gen_legal_moves(x, y, board_size):
    new_moves = []
    move_off_sets = [(-1, -2), (-1, 2), (-2, 1), (-2, -1),
                     ( 1, -2), ( 1, 2), ( 2, 1), ( 2,-1)]

    for i in move_off_sets:
        new_x = x + i[0]
        new_y = y + i[1]
        if legal_coord(new_x, board_size) and legal_coord(new_y, board_size):
            new_moves.append((new_x, new_y))

    return new_moves

def legal_coord(x, board_size):
    if x > 0 and x < board_size:
        return True
    else:
        return False


k = knights_graph(3)

def knights_tour(n, path, u, limit):
    u.set_color('white')
    path.append(u)

    if n < limit:
        nbr_list = list(u.get_connection())
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].get_color() == 'white':
                done = knights_tour(n+1, path, nbr_list[i], limit)
                i += 1
        if not done:
            path.pop()
            u.set_color('white')
    else:
        done = True

    return done

knights_tour(0, [], k.get_vertex(1), 6)

