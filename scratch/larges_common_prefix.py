words = ["geeksforgeeks", "geeks", "geek", "geezer"]

def largest_common_prefix(word_array):
	min_len = _get_min_len(word_array) #O(n)

	prefix = ''
	for i in range(min_len): #O(m)
		letters = [word[i] for word in words] #O(n)
		letter_set = set(letters)
		if len(letter_set) == 1:
			prefix += letter_set.pop()

	return prefix

#O(nm)
# n - number of string
# m - length of shortest string

def _get_min_len(word_array):
	min_len = float('inf')
	for word in words:
		if len(word) < min_len:
			min_len = len(word)

	return min_len




### Could use a trie 
### one by one add each word to a trie
### from root traverse tree until we find a nod having more than 1 children or 0 children





def largest_common_prefix(word_array):
	if len(word_array) == 0:
		return None

	if len(word_array) == 1:
		return word_array[0]

	count = 0
	while True:
		let = [i[count] for i in word_array]
		let_set = set(let)
		if len(let_set) == 1:
			count += 1
		else:
			break

	return count

print largest_common_prefix(words)




