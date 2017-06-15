import sys


class KnightsTour:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.board = []
        self.generate_board()


    def generate_board(self):
        """
        Creates nested list to represent the game board
        """
        for i in range(self.h):
            self.board.append([0]*self.w)

    def print_board(self):
        print "  "
        print "------"
        for elem in self.board:
            print elem
        print "------"
        print "  "

    def generate_legal_moves(self, cur_pos):
        """
        Generate list of legal moves for knight
        """

        possible_moves = []
        move_off_sets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                         (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in move_off_sets:
            new_x = cur_pos[0] + move[0]
            new_y = cur_pos[1] + move[1]

            if new_x >= self.h or new_x < 0:
                continue
            elif new_y >= self.w or new_y < 0:
                continue
            else:
                possible_moves.append((new_x, new_y))

        return possible_moves

    def sort_lonely_neighbord(self, to_visit):
        """
         More efficient to visit lonely neighbors first, because edges of the chessboard
         cannot be reached easily if done later in traversal
        """

        neighbor_list = self.generate_legal_moves(to_visit)
        empty_neighbours = []

        for neighbor in neighbor_list:
            value = self.board[neighbor[0]][neighbor[1]]
            if value == 0:
                empty_neighbours.append(neighbor)

        scores = []
        for empty in empty_neighbours:
            score = [empty, 0]
            moves = self.generate_legal_moves(empty)
            print moves
            for m in moves:
                if self.board[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)

        scores_sort = sorted(scores, key=lambda s:s[1])
        sorted_neighbors = [s[0] for s in scores_sort]
        return sorted_neighbors


    def tour(self, n, path, to_visit):
        """
        n = current depth of search tree
        path = current path taken
        to_visit = node to visit
        """
        self.board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit)
        print "Visiting: ", to_visit


        if n == self.w * self.h:
            self.print_board()
            print path
            print "Done"
            sys.exit(1)

        else:
            sorted_neighbors = self.sort_lonely_neighbord(to_visit)
            for neighbor in sorted_neighbors:
                self.tour(n+1, path, neighbor)

            ### If loop exited then we reset
                self.board[to_visit[0]][to_visit[1]] = 0
            try:
                path.pop()
                print "going back to ", path[-1]
            except IndexError:
                print "no path found"
                sys.exit(1)


kt = KnightsTour(8, 8)
kt.print_board()
kt.tour(1, [], (0,0))

