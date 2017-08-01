import sys
class Board:
    def __init__(self, height, width):
        self.board = [[0] * width for _ in range(height)]

    def set_value(self, pos, value):
        x, y = pos
        self.board[x][y] = value

    def get_value(self, pos):
        x, y = pos
        return self.board[x][y]

    def print_board(self):
        print "\n"
        for line in self.board:
            print line
        print "\n"


class KnightsTour:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = Board(height, width)

    def _get_legal_moves(self, pos):
        x, y = pos
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                       (2, 1), (2, -1), (-2, 1), (-2, -1)]
        #move_offsets = [(1, 1), (1, -1), (-1, 1), (-1, -1),
        #                (0, 1), (0, -1), (1, 0), (-1, 0)]

        moves = []
        for offset in move_offsets:
            new_x = x + offset[0]
            new_y = y + offset[1]
            if new_x < 0 or new_x >= self.height:
                continue
            elif new_y < 0 or new_y >= self.width:
                continue
            else:
                moves.append((new_x, new_y))

        return moves

    def get_lonely_neighbors(self, pos):
        legal_moves = self._get_legal_moves(pos)

        lonely_neighbors = []
        for legal_move in legal_moves:
            if self.board.get_value(legal_move) == 0:
                score = [legal_move, 0]
                neighbors = self._get_legal_moves(legal_move)
                for neighbor in neighbors:
                    if self.board.get_value(neighbor) == 0:
                        score[1] += 1
                lonely_neighbors.append(score)
        sorted_lonely_neighbor = sorted(lonely_neighbors, key = lambda k: k[1])
        sorted_lonely_neighbor = [x[0] for x in sorted_lonely_neighbor]

        return sorted_lonely_neighbor

    def tour(self, level, path, to_visit):
        self.board.set_value(to_visit, level)
        path.append(to_visit)

        print "visiting: ", to_visit

        if level == self.height * self.width:
            print "Done"
            self.board.print_board()
            print path
            sys.exit(1)
        else:
            neighbors = self.get_lonely_neighbors(to_visit)
            for neighbor in neighbors:
                self.tour(level +1, path, neighbor)

            # If this loop is exited then all neighbors failed and we must step back once
            self.board.set_value(to_visit, 0)
            try:
                print path
                path.pop()
                print "Going back to: ", path[-1]
            except IndexError:
                print "No path found"
                self.board.print_board()
                sys.exit(1)



k = KnightsTour(8, 8)
k.tour(1, [], (7,7))



