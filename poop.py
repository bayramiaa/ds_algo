import sys

class Board:
	def __init__(self, height, width):
		self.board = [[0]*width for _ in range(height)]

	def set_value(self, pos, value):
		x = pos[0]
		y = pos[1]

		self.board[x][y] = value

	def get_value(self, pos):
		x = pos[0]
		y = pos[1]

		return self.board[x][y]

	def print_board(self):
		print "\n"
		for line in self.board:
			print line
		print "\n"

class KnightsTour:
	def __init__(self, height, width):
		self.board = Board(height, width)
		self.height = height
		self.width = width

	def _gen_moves(self, pos):
		moves = []
		move_offsets = [(1, 2), (1, -2), (2, 1), (2, -1),
			     	    (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

		for offset in move_offsets:
			new_x = pos[0] + offset[0]
			new_y = pos[1] + offset[1]

			if new_x < 0 or new_x >= self.width:
				continue
			elif new_y < 0 or new_y >= self.height:
				continue
			else:
				moves.append((new_x, new_y))

		return moves

	def gen_legal_moves(self, pos):
		legal_moves = []
		moves = self._gen_moves(pos)
		
		for move in moves:
			if self.board.get_value(move) == 0:
				legal_moves.append(move)

		return legal_moves

	def tour(self, level, visited, to_visit):
		self.board.set_value(to_visit, level)
		visited.append(to_visit)

		if level == self.height * self.width:
			print "done"
			self.board.print_board()
			print visited
			sys.exit(1)
		else:
			legal_moves = self.gen_legal_moves(to_visit)

			for move in legal_moves:
				self.tour(level + 1, visited, move)

				# if i exit this loop then move selected did not work
				print 'fail'
				self.board.set_value(to_visit, 0)
				try:
					visited.pop()
				except IndexError:
					print "no path found"
					sys.exit(1)




k = KnightsTour(8,8)
k.tour(1, [], (3,0))




##########################################################################################################################
### Write some Python code to take a list of words as input and return the words and their anagrams as output. 
### Anagram: rearranging the letters of a word to produce a new word using all the original letters exactly once
###
### example_list = ['cat', 'lemon', 'act', 'swim', 'melon']
### output: [('cat', 'act'), ('lemon', 'melon')]
###
### No need to import any libraries, just use basic python objects.
##########################################################################################################################

from collections import defaultdict
word_list = ['army', 'mary', 'cool', 'dude', 'listen', 'silent', 'listens']

def group_anagrams(word_list):
    anagram_dict = defaultdict(list)
    
    for word in word_list: # O(n)
        sorted_letters = ''.join(sorted(word)) #O(klogk)
        anagram_dict[sorted_letters].append(word)
    
    response = []
    for value in anagram_dict.values(): #O(m)
        if len(value) > 1:
            response.append(tuple(value))
    
    return response
    
#print group_anagrams(word_list)
# k >> n

def group_anagrams(word_list):
    dict_list = []
    
    for word in word_list: #O(n)
        word_dict = {}
        for letter in word: #O(k)
            word_dict[letter] = word_dict.get(letter, 0) + 1
        dict_list.append(word_dict)
    
    response = []
    for i in range(len(word_list)): #O(n)
        anagram_list = [word_list[i]]
        for j in range(i + 1, len(dict_list)):# O(n)
            if dict_list[i] == dict_list[j]:
                anagram_list.append(word_list[j])
            
        if len(anagram_list) > 1:
            response.append(tuple(anagram_list))
            
    return response

print group_anagrams(word_list)



date_id        vendor    product    sold     returned
2016-10-01    alpha    prod_a    100        5
2016-10-01    alpha    prod_a    100        5
2016-10-01    alpha    prod_a    100        5
2016-10-01    alpha    prod_b    20        0
2016-10-01    alpha    prod_c    200        0
2016-10-01    beta    prod_d    50        10
2016-10-01    beta    prod_d    50        10
2016-10-01    beta    prod_d    50        10
2016-10-01    beta    prod_e    35        5
2016-10-01    gamma    prod_h    100        10
2016-10-02    alpha    prod_b    75        10
2016-10-02    alpha    prod_c    100        10
2016-10-02    alpha    prod_f    45        15
2016-10-02    beta    prod_e    95        10
2016-10-02    gamma    prod_h    90        0
2016-10-03    alpha    prod_a    65        5
2016-10-03    alpha    prod_c    50        15
2016-10-03    alpha    prod_g    50        20
2016-10-03    beta    prod_d    80        5
2016-10-03    beta    prod_e    200        0
2016-10-03    gamma    prod_h    100        10

SELECT *
FROM(
    SELECT *, COUNT(1) counts
    FROM SALES_FACT
    GROUP BY date_id, vendor, product, sold, returned
    )
WHERE counts > 1;

Sales Fact Table
sales_fact_id
date_id
vendor_id
product_id
sold
net_sold (sold - returned)



