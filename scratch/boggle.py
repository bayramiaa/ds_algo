board = [['G','I','Z'],
		  ['U','E','K'],
	      ['Q','S','E']]

words = ['GEEKS', 'FOR', 'QUIZ', 'GO']

class Board:
	def __init__(self, letter_array):
		self.board = letter_array
		self.size = len(letter_array)

	def get_letter(self, pos):
		return self.board[pos[0]][pos[1]]


class Boggle:
	def __init__(self, board, words):
		self.board = board
		self.words, self.prefixes  = self.load_words(words)

	def load_words(self, words):
		word_set = set()
		prefix_set = set()

		for word in words:
			word_set.add(word)
			for i in range(len(word)):
				prefix_set.add(word[:i])
		return word_set, prefix_set

	def is_prefix(self, prefix):
		if prefix in self.prefixes:
			return True
		else:
			return False

	def is_word(self, word):
		if word in self.words:
			return True
		else:
			return False

	def generate_moves(self, pos):
		legal_moves = []
		move_offsets = [(1,0), (-1,0), (0, 1), (0, -1),
			            (1, 1), (1, -1), (-1, 1), (-1, -1)]

		for offset in move_offsets:
			new_x = pos[0] + offset[0]
			new_y = pos[1] + offset[1]

			if new_x < 0 or new_x >= self.board.size:
				continue
			elif new_y < 0 or new_y >= self.board.size:
				continue
			else:
				legal_moves.append((new_x, new_y))
		return legal_moves

	def check_board(self, pos):
		stack = [(to_visit, [pos], self.board.get_letter(pos)) for to_visit in self.generate_moves(pos)]
		
		words = set()
		while stack:
			curr, path, chars = stack.pop()
			curr_char = self.board.get_letter(curr)
			curr_chars = chars + curr_char

			if curr_chars in self.words:
				words.add(curr_chars)

			if curr_chars in self.prefixes:
				adj_moves = self.generate_moves(curr)

				new_moves = [(to_visit, path + [curr], curr_chars) for to_visit in adj_moves if to_visit not in path]
				for move in new_moves:
					stack.append(move)

		return words

	def run(self):
		words = set()
		for i in range(self.board.size):
			for j in range(self.board.size):
				words |= self.check_board((i,j))

		return words
		
board = Board(board)
b = Boggle(board, words)
b.run()
