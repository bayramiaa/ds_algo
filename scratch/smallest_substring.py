"""
Input :  string = "this is a test string"
         pattern = "tist"
Output :  Minimum window is "t stri"
"""
_input = "this is a test string"
_pattern = "tist"
import string


def smallest_substring(str1, pat):
	if len(str1) < len(pat):
		return None

	str_dict = dict.fromkeys(string.ascii_lowercase + ' ', 0)
	pat_dict = dict.fromkeys(string.ascii_lowercase + ' ', 0)
	for char in pat:
		pat_dict[char] += 1

	start = 0
	start_index = -1
	min_len = float('inf')
	char_count = 0

	for i in range(len(str1)):
		str_dict[str1[i]] += 1

		if (pat_dict[str1[i]] != 0) and (str_dict[str1[i]] <= pat_dict[str1[i]]):
			char_count += 1

		if char_count == len(pat):
			while (str_dict[str1[start]] > pat_dict[str1[start]]) or (pat_dict[str1[start]] == 0):
				
				if (str_dict[str1[start]] > pat_dict[str1[start]]):
					str_dict[str1[start]] -= 1
					start +=1 
					


			len_window = i - start + 1

			if (min_len > len_window):
				min_len = len_window
				start_index = start
	return str1[start_index:(start_index + min_len)]

smallest_substring(_input, _pattern)



from collections import Counter

def get_all_substrings(input_string):
	length = len(input_string)
	return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]


substring =  get_all_substrings('this is a test string')

#ef same_except1(s1, s2):
#   ct1, ct2 = Counter(s1), Counter(s2)
#   return sum((ct1 - ct2).values()) == 1 and sum((ct2 - ct1).values()) == 1

#or word in x:
	
#	print str_count

c1 = Counter(' string')
c2 = Counter(' strin')

#est_count = Counter("tist")