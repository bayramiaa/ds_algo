"""
On a smartphone, you are given a touchpad similar to below for entering password:

1  |  2  |  3
-------------
4  |  5  |  6
-------------
7  |  8  |  9

passwords are created by continuously swiping your finger, without lifting it, over the touchscreen keyboard.

Write a program to return the total number of passwords that are possible. Individual passwords not required to be returned by the program..

The constraints are:
The passwords can be from 1 to 9 character long
You can move along any direction, including diagonal
While swiping, the finger can not be lifted. So, 123 is a valid password. 13 is invalid. 159 is valid. 19 is invalid.
The same character can not be repeated. So, 123 is a valid password. 121 is invalid.
"""

# create touchpad 
# return all neighbors from a position


class Touchpad:
	def __init__(self):
		self.touchpad = [[1, 2], [3, 4]]

	def get_value(self, pos):
		return self.touchpad[pos[0]][pos[1]]




class Touchpad:
	def __init__(self):
		self.touchpad = [[1, 2], [3, 4]]

	def get_value(self, pos):
		return self.touchpad[pos[0]][pos[1]]


class Password:
	def __init__(self, height, width):
		self.height = height
		self.width = width

	def generate_possible_moves(self, pos):
		move_offsets = [(0, 1), (0, -1), ( 1, 0), (-1,  0),
		   	            (1, 1), (1, -1), (-1, 1), (-1, -1)]

		possible_moves = []
		for offset in move_offsets:
			new_x = pos[1] + offset[1]
			new_y = pos[0] + offset[0]

			if new_x < 0 or new_x >= self.width:
				continue
			if new_y < 0 or new_y >= self.height:
				continue
			else:
				possible_moves.append((new_y, new_x))

		return possible_moves

	def generate_legal_moves(self, pos, visited_nodes):
		moves = self.generate_possible_moves(pos)

		legal_moves = []
		for move in moves:
			if move not in visited_nodes:
				legal_moves.append(move)
		return legal_moves

	def get_passwords(self, pos, visited_keys, password):
		password.append(pos)
		visited_keys[pos] = 1
		legal_moves = self.generate_legal_moves(pos, visited_keys)

		print "posistion", pos
		print visited_keys
		print legal_moves
		print password

		while legal_moves:
			password
			move = legal_moves.pop()
			self.get_passwords(move, visited_keys, password)

		return password




	def run(self):
		starting_pos = (0,0)
		passwords = [starting_pos]
		moves = self.generate_possible_moves(starting_pos)

		print moves
		count = 0
		for move in moves:
			visited = {starting_pos: 1}
			visited[move] = 1
			password = [starting_pos, move]

			move_queue = self.generate_legal_moves(move, visited)
			print count
			print move_queue
			count += 1
			for i in move_queue:
				stuff = self.get_passwords(i, visited, password)
				#print [t.get_value(i) for i in stuff]

t = Touchpad()
p = Password(2, 2)
#print p.generate_legal_moves((0,1), {(0,0): 1})
print p.run()

### Brute force
### 1 - write method that generates all possible moves and checks if they are on the board
### 2 - write method that checks if new move has any repeats, if so do not add repeats to next possible moves
### 3 - run method that 


"""
1 | 2
-----
3 | 4

possible passwords for (0,0): [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 2, 4, 3]
								    [1, 3], [1, 3, 2], [1, 3, 2, 4], [1, 3, 4], [1, 3, 4, 2]
								    [1, 4], [1, 4, 2], [1, 4, 2, 3], [1, 4, 3], [1, 4, 3, 2]]

starting position (0,0): 
	pass1:
		current_value = [1]
		current_passwords = [1] ## this gets appended when running thr
		moves_to_check (some Q) = 2, 3, 4
	pass2:
		current_value = [1,2]
		current_passwords = [[1], [1,2]]
		moves_to_check = 3, 4, 

"""


current - (0,0)
new - [(0, 1), (1, 0), (1, 1)]


r1
	[(0,0), (1,0)]
r2
	[(0,0), (0,1)]
r3
	[(0,0), (1,1)]




