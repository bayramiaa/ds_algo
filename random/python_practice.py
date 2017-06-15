def find_word_count(sentence):
	all_words = sentence.split()
	return len(all_words)

def find_count_of_words(sentence):
	words = sentence.split()
	word_count = {}

	for word in words:
		word_count[word] = word_count.get(word, 0) + 1
	return word_count

def get_max(array):
	max_int = 0
	for integer in array:
		if integer > max_int:
			max_int = integer
	return max_int

def get_median(array):
	q, r = divmod(len(array), 2)
	# divmod(5,2) = 2,1
	if r:
		return array[q]
	return (array[q] + array[q-1]) / 2.0
get_median([1,2,3,4])

def first_non_reocurring(array):
	order = []
	counts = {}

	for num in array:
		if num in counts:
			counts[num] += 1
		else:
			counts[num] = 1
			order.append(num)

	for num in order:
		if counts[num] == 1:
			return num

	return None

def most_reocurring_number(array):
	counts = {}

	for num in array:
		counts[num] = counts.get(num,0) + 1

	items = counts.items()
	sorted_items = sorted(items, key = lambda w: w[1], reverse=True)[0]

	return sorted_items[0]


def find_minimum_distance(array):
	w  = []
	for i in range(len(x)):
		for j in range(1,len(x)):
			if i != j:
				min_distance = abs(x[i] - x[j])
				w.append(min_distance)

	return min(w)

def greatest_common_factor(x,y):
	smaller = min(x,y)

	for i in range(1, smaller + 1):
		if ((x % i == 0) and (y % i == 0)):
			gcf = i

	return gcf

def find_string(string,dic):
	for i in range(len(string)):
		for j in range(1,len(string) + 1):
			word = string[i:(i+j)]
			print word
			if word in dic:
				dic[word] = dic.get(word,0) + 1
	return dic


def simple_sort(array):
	for i in range(1, len(x)):
		position = i
		current_value = array[i]

		while position > 0 and array[position -1] > current_value:
			array[position] = array[position - 1]
			position = position - 1

		array[position] = current_value
	return array


def simple_search(array, t):
	found = False
	count = 0
	while not found and count < len(array):
		print count
		if array[count] == t:
			found = True
		count +=1
	return found



def binary_search(array, t):
	first = 0
	last = len(array) - 1
	found = False

	while first < last and not found:
		middle = (first + last) / 2
		print (first,last,middle)
		if array[middle] == t:
			found = True

		if t > array[middle]:
			first += 1
		else:
			last -= 1

	return found


x = [1,2,3,4,5,7,8,9]

binary_search(x, 6)



def merge_arrays(a,b):
	c = []

	while len(a) >0 and len(b) > 0:
		if a[0] < b[0]:
			c.append(a[0])
			a.remove(a[0])
		else:
			c.append(b[0])
			b.remove(b[0])

	if len(a) == 0:
		 c += b
	else:
		c += a
	return c 

def merge_sort(array):
	if len(array) <= 1:
		return array

	middle = (len(array)) / 2
	a = merge_sort(array[middle:])
	b = merge_sort(array[:middle])
	return merge_arrays(a,b)

merge_sort([22,2,4,1,3,34,21,14,55])


### Coin change problem
### Find minimum number of coins needed to reach change
coins = [1,5,10]
change = 60
### 
def naive_coin_change(coins, change):
	min_coins = change
	if change in coins:
		return 1

	for coin in [i for i in coins if i < change]:
		curr_coins = 1 + naive_coin_change(coins, change - coin)

		if curr_coins < min_coins:
			min_coins = curr_coins
	return min_coins
naive_coin_change(coins,change)

def naive_coin_change(coins, change):
	if change in coins:
		return 1

	for coin in [i for i in coins if i < change]:
		curr_coins = 1 + naive_coin_change(coins, change - coin)


## Dynamic solution


coins = [1,5,10]
change = 190
def semi_dynamic_coin_change(coins, change, mem):
	if change in coins:
		return 1
	elif mem[change] > 0:
		return mem[change]
	else:
		for coin in [i for i in coins if i < change]:
			num_coins = 1 + semi_dynamic_coin_change(coins, change - coin, mem)

			if num_coins < change:
				mem[change] = num_coins
	return num_coins

semi_dynamic_coin_change(coins,change,[0] * (change + 1))





## find runtime
def is_palindrom(string):
	if len(string) <= 1:
		return True

	first = string[0]
	last = string[-1]

	if first != last:
		return False

	return is_palindrom(string[1:len(string)-1])

### 2sum
# can there be duplicates elements? more than 1 solution? or more than 1 + duplicate
#n^2
def naive_find_pair_sum(array, t):
	response = []
	for i,n in enumerate(array): #n 
		for j,n in enumerate(array[i+1:]): #n
			pair = (array[i], array[j + 1])
			if sum(pair) == t:
				response.append(pair)
	return response

def twoSum(nums, target):
    if len(nums) <=1:
        return False
    
    hold = {}
    for i, num in enumerate(nums):
        if num in hold:
            return [hold[num], num]
        else:
            hold[target - num] = num
	            

better_find_pair_sum([1,1,2,2,1,1,3],2)



### 3SUM problems 
x = [4,2,1,3,4,12,1,7]
### n^3
def naive_find_triplets_sum(array, target):
	response = []
	for i in range(len(array)): #n
		for j in range(i+1, len(array)): #n
			for k in range(j+1, len(array)): #n
				triplet = (array[i], array[j], array[k])
				print triplet
				if sum(triplet) == target:
					response.append(triplet)
	return response
naive_find_triplets_sum(x,9)


## find runtime
def better_find_triplets_sum(array, target):
	array.sort() #O(nlogn)
	response = []
	for i in range(len(array)-2):
		x = i
		y = i + 1
		z = len(array) - 1

		if array[x] + array[y] + array[y + 1] > target: # small optimization
			return response

		while y != z:
			triplet = (array[x], array[y], array[z])
			if sum(triplet) == target:
				response.append(triplet)
				y += 1
				z -+ 1
			elif sum(triplet) < target:
				y +=1
			else:
				z -=1
	return response



#subset sum problem
#As others mention this is an NP-hard problem. It can be solved in exponential time O(2^n),
response = []
def subset_sum_k(array, target, partial = []):
	if sum(partial) == target:
		response.append(partial)
	if sum(partial) > target:
		return

	for i in range(len(array)):
		n = array[i]
		remaining = array[i+1:]
		subset_sum_k(remaining, target, partial + [n])
	return response

subset_sum_k(range(10), 8)



## find sub array with greatest sum
array = [1,-3,14,-2,5,2,3]
def find_greatest_array(array):
	greatest_sum = None

	for i in range(len(array)):
		for j in range(i + 1,len(array) + 1):
			array_sum = sum(array[i:j])
			if array_sum > greatest_sum:
				greatest_sum = array_sum
				greatest_array = array[i:j]
	return greatest_array

find_greatest_array(array)


### find subset array that sum to target
x = [1,2,4,5,2,2,12]
target = 11
def find_subset_sum(array, target):
	for i in range(len(x)):
		for j in range(1, len(x) + 1):
			if sum(x[i:j]) == target:
				return x[i:j]
	return None
find_subset_sum(x,target)



#### brackets closed
def check_bracket(bstring):
	holder = []
	balanced = True
	index = 0

	while balanced and index < len(bstring):
		symbol = bstring[index]
		if symbol == "(":
			holder.append(symbol)
		else:
			if len(holder) == 0:
				balanced = False
			else:
				holder.pop()
		index += 1

	if balanced and len(holder) == 0:
		return True
	else:
		return False


check_bracket("((()()))") == True
check_bracket("((())") == False



###Dedup a list (remove duplicates). 

x = [1,2,3,3,1,2,4]
def dedup_list(array):
	r = []
	for i in range(len(array)):
		if array[i] not in r:
			r.append(i)
	return r
dedup_list(x)




#A hash table is a collection of items which are stored in such a way as to make it easy to find them later.

def del_dups(seq):
    seen = {}
    pos = 0
    for item in seq:
        if item not in seen:
            seen[item] = True
            seq[pos] = item
            print seen
            print seq
            pos += 1
    del seq[pos:]

del_dups([1,2,2,2,3,4,5,1,6])




def factorial(num):

	if num <=1:
		return 1

	return num * factorial(num - 1)

factorial(3)


def int_to_string(n, base):
	convString = "0123456789"

	if n < base:
		return convString[n]
	else:
		q, r = divmod(n, base)
		return int_to_string(q, base) + convString[r]

int_to_string(12345, 2)

st = 'reverse'
def reverse_string(s):
	if len(s) <= 1:
		return s
	else:
		return  reverse_string(s[1:]) + s[0] 

reverse_string(st)

def is_palindrome(word):

	if len(word) <= 1:
		return True

	if word[0] != word[-1]:
		return False

	return is_palindrome(word[1:-1])


import heapq
def find_kth_larget(nums, k):
	heap = []
	for num in nums:
		heapq.heappush(heap, num) #O(nlogn)
	for _ in xrange(len(nums) - k):
		heapq.heappop(heap) #O((n-k)logn)
	return heapq.heappop(heap)


def find_kth_larget(nums, k):
	heapq.heapify(nums) #O(n)

	for i in range(len(nums) - k): #O((n-k)log(n))
		heapq.heappop(nums)

	return heapq.heappop(nums)




def perm(array, target, partial = []):
	if sum(partial) == target:
		print partial

	for i in range(len(array)):
		n = array[i]
		remainder = array[i+1:]
		perm(remainder, target, partial + [n])
		

"""
find number of ways change can be made
"""

coins = [1,5, 10, 25]
amount = 30

def coin_change_2(amount, coins):
	dp = [0] * (amount + 1)
	dp[0] = 1

	for coin in coins:
		for change in range(1, amount + 1):
			if change >= coin:
				dp[change] += dp[change - coin]

	return dp
coin_change_2(amount, coins)