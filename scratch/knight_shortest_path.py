class KnightShortestPath:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def gen_legal_moves(self, pos):
        x, y = pos

        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                       (2, 1), (2, -1), (-2, 1), (-2, -1)]

        legal_moves = []
        for move in move_offsets:
            new_x = x + move[0]
            new_y = y + move[1]

            if new_x < 0 or new_x >= self.height:
                continue
            elif new_y < 0 or new_y >= self.width:
                continue
            else:
                legal_moves.append((new_x, new_y))

        return legal_moves

    def run(self, starting_pos, goal, dist, ways):
        queue = [starting_pos]

        dist[starting_pos] = 0
        ways[starting_pos] = 1

        while queue:
            cur = queue.pop(0)
            if cur == goal:
                print "reached goal in %d moves and %d ways"%(dist[cur], ways[cur])
                return

            legal_moves = self.gen_legal_moves(cur)
            for move in legal_moves:
                if move in dist and dist[move] == dist[cur] + 1:
                    ways[move] += ways[cur]
                if move not in dist:
                    dist[move] = dist[cur] + 1
                    ways[move] = ways[cur]
                    queue.append(move)


k = KnightShortestPath(8,8)
k.run((0,0), (0,2), {}, {})




# queue = [(1,1)]
# dist[(1,1)] = 0 ; {(1,1) : 0}
# ways[(1,1)] = 1 ; {(1,1) : 1}

# while len(queue):
# cur = queue.pop(0)

# if cur == goal:
# print "reached goal in %d moves and %d ways"

#else:
# for move in moves
# if move in dist