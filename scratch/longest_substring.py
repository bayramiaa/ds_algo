"""
input: ["ababb", "abb"]
output:  3 (longest substring in both is 'abb')
"""

#    a b b 
#  0 0 0 0 
#a 0 1 0 0 
#b 0 0 2 1
#a 0 1 0 0 
#b 0 0 2 1
#b 0 0 1 3

# 0 - create (m+1)x(n+1) matrix
# 1 - for each letter in word 1 compare to letters in word 2
# 2 - if letter matches in word one then update the position on the grid
# 	  by checking the letter up and to the left one + 1
# 3 - store the length of longest patters
# 4 - store where the longest pattern ends
# 5 - return word1[(pattern_ending - longest):pattern_ending]


def longest_subsrting(s1, s2):
	m = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
	
	longest = 0
	i_longest = 0
	for i in range(1, len(s1) + 1):
		for j in range(1, len(s2) + 1):
			if s1[i - 1] == s2[j - 1]:
				m[i][j] = m[i-1][j-1] + 1
				if m[i][j] > longest:
					longest = m[i][j]
					i_longest = i
	return s1[(i_longest-longest):i_longest]



print longest_subsrting("ababb", "abb")