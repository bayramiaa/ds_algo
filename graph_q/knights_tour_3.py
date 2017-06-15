import sys


class KnightsTour:
    def __init__(self, board_size):
        self.board_size = board_size

        self.board = []
        self.generate_board()

    def generate_board(self):
        for i in range(self.board_size):
                self.board.append([0]*self.board_size)

    def print_board(self):
        print ""
        for row in self.board:
            print row
        print ""

    def gen_legal_moves(self, cur_pos):
        possible_moves = []
        move_offsets = [(-2,-1), (-2,1), (-1, 2), (-1, -2),
                         ( 2,-1), ( 2,1), ( 1, 2), (1, -2)]

        for move in move_offsets:
            new_x = cur_pos[0] + move[0]
            new_y = cur_pos[1] + move[1]

            if new_x >= self.board_size or new_x < 0:
                continue
            elif new_y >= self.board_size or new_y < 0:
                continue
            else:
                possible_moves.append((new_x, new_y))

        return possible_moves

    def sort_lonely_neighbor(self, to_visit):

        neighbor_list = self.gen_legal_moves(to_visit)
        empty_neighbors = []

        for neighbor in neighbor_list:
            if self.board[neighbor[0]][neighbor[1]] == 0:
                empty_neighbors.append(neighbor)

        scores = []
        for empty in empty_neighbors:
            score = [empty, 0]
            moves = self.gen_legal_moves(empty)

            for move in moves:
                if self.board[move[0]][move[1]] == 0:
                    score[1] += 1
            scores.append(score)

        sorted_scores = sorted(scores, key=lambda x: x[1])
        scored_neighbors = [s[0] for s in sorted_scores]

        return scored_neighbors



    def tour(self, n, path, to_visit):
        """
        n = current depth of search tree
        path = current path taken
        to_visit = node to visit
        """
        print to_visit
        self.board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit)

        if n == self.board_size **2:
            self.print_board()
            print "Done"
            sys.exit(1)
        else:
            sorted_neighbors = self.sort_lonely_neighbor(to_visit)
            for neighbor in sorted_neighbors:
                self.tour(n+1, path, neighbor)
                ## IF loop exited then reset
                self.board[to_visit[0]][to_visit[1]] = 0
            try:
                path.pop()
            except IndexError:
                print "no path found"
                sys.exit(1)






k = KnightsTour(8)
k.print_board()
k.tour(1, [], (0,0))
