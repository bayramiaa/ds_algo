## find words in a long string
string = 'cata'
dic = {"cat":0, "j":0, "fart":0,"nt":0}

def find_string(string,dic):
	for i in range(len(string)):
		for j in range(1,len(string) + 1):
			word = string[i:(i+j)]
			print word
			if word in dic:
				dic[word] = dic.get(word,0) + 1
	return dic

find_string(string,dic)


## find ordered set that sums to a target
x = [1,2,1,1,3,1]

def get_target_sum(array, target):
	response = []
	for i in range(len(array)):
		for j in range(i + 1, len(array)+1):
			tmp = x[i:j]
			print tmp
			if sum(tmp) == target and tmp not in response:
				response.append(tmp)
	return response

print get_target_sum(x, 4)


## find the max sub_array
x = [1, -2, 3, 10, -4, 7, 2, -5]

def max_sub_array(array):
	max_sum_sub = 0
	max_sub_array = []
	for i in range(len(x)): #n
		for j in range(1,len(x) + 1): #n
			sub_array = array[i:i+j]
			sum_sub_array = sum(sub_array)
			if sum_sub_array > max_sum_sub:
				max_sum_sub = sum_sub_array
				max_sub_array = sub_array
	return (max_sum_sub, max_sub_array)
max_sub_array(x)


# simple sort
def simple_sort(array):
	for i in range(1, len(array)):
		current_value = array[i]
		position = i
		while position > 0 and array[position-1] > current_value:
			array[position] =  array[position - 1]
			position = position - 1

		array[position] = current_value

	return array

# binary search
def binary_search(ordered_array, item):
	first = 0
	last = len(ordered_array)
	found = False

	while first < last and not found:
		middle = (first + last) // 2
		if ordered_array[middle] == item:
			found = True

		if item < ordered_array[middle]:
			last = last - 1
		else:
			first = first + 1
	return found

# simple search
def linear_search(unordered_array, item):
	found = False
	count = 0
	while not found and count <= len(unordered_array):
		if unordered_array[count] == item:
			found = True
		count += 1
	return	found




x = [1,1,2,2,3,4]

def find_3_elements_sub(array, x):
	answers = []
	for i in range(len(array)): # 0 1 2 3 4
		for j in range(1, len(array)): # 1 2 3 4
			for k in range(2, len(array)): # 2 3 4
				print (array[i], array[j], array[k])
				sum_sub = array[i] + array[j] + array[k]
				if sum_sub == x:
					answers.append([array[i],array[j],array[k]]) 
	return answers

"""
median 2 sorted arrays
"""


def permutation(s):
   if len(s) == 1:
     return [s]

   perm_list = [] # resulting list
   for a in s:
     remaining_elements = [x for x in s if x != a]
     z = permutation(remaining_elements) # permutations of sublist

     for t in z:
       perm_list.append([a] + t)

   return perm_list


"""
coin change
"""
coins = [1,5,10]
change = 190
def coin_change(coins, change, mem):
	if change in coins:
		mem[change] = 1
		return 1
	if mem[change] > 0:
		return mem[change]


	for coin in [i for i in coins if i < change]:
		curr_coins = 1 + coin_change(coins, change - coin, mem)

		if curr_coins < change:
			mem[change] = curr_coins

	return curr_coins

coin_change(coins, change, [0] * (change + 1))


def coin_change(coins, change):
	if change in coins:
		return 1

	for coin in [i for i in coins if i < change]:
		curr_coins = 1 + coin_change(coins, change - coin)

	return curr_coins

coin_change(coins, 4)

















def permutation(items):
	if len(items) == 1:
		return [items]

	results = []
	for item in items:
		remaining_elements = [i for i in items if i != item]
		z = permutation(remaining_elements)

		for t in z:
			results.append(t + [item])

	return results

permutation([1,2,3])


































