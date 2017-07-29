s1 = 'geeksforgeeks'
s2 = 'geeksswrgeeks'



def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): 
                	answer = match
                match = ""
    return answer

print longestSubstringFinder(s1, s2)
print longestSubstringFinder("apples", "appleses")
print longestSubstringFinder("bapples", "cappleses")


def longest_common_substring(s1, s2):
   m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
   longest = 0
   x_longest = 0
   for x in xrange(1, 1 + len(s1)):
       for y in xrange(1, 1 + len(s2)):
           if s1[x - 1] == s2[y - 1]:
               m[x][y] = m[x - 1][y - 1] + 1
               if m[x][y] > longest:
                   longest = m[x][y]
                   x_longest = x
           else:
               m[x][y] = 0
   return s1[x_longest - longest: x_longest]

longest_common_substring(s1,s2)

















def lcs_c(str1, str2):
	m = len(str1)
	n = len(str2)
	counter = [[0]*(n+1) for x in range(m+1)]
	longest = 0
	lcs_set = set()

	for i in range(m): #O(n)
		for j in range(n): #O(n)
			if S[i] == T[i]:
				c = counter[i][j] + 1
				if c > longest:
					lcs_set = set()
					longest = c
					lcs_set.add(S[i-c+1:i+1])
				elif c == longest:
					lcs_set.add(S[i-c+1:i+1])
	return lcs_set

lcs(s1, s2)



def lcs_c(X, Y, m, n): ## O(2^n)
 
    if m == 0 or n == 0:
       return 0;
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1);
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))