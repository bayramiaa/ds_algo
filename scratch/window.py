"""
Input :  string = "this is a test string"
         pattern = "tist"
Output :  Minimum window is "t stri"
Explanation: "t stri" contains all the characters
              of pattern.
"""


_input_string = "this is a test string"
_input_pattern = "tist"

import string

def shortest_substring(s, p):
    if len(p) > len(s):
        return None

    s_dic = dict().fromkeys(string.ascii_letters.lower() + ' ', 0)
    p_dic = dict().fromkeys(string.ascii_letters.lower() + ' ', 0)

    for letter in p:
        p_dic[letter] += 1


    char_count = 0
    start = 0
    start_index = -1
    min_len = float('inf')

    for i in range(len(s)): #add letter from string int dic
        s_dic[s[i]] += 1

        if (s_dic[s[i]] <= p_dic[s[i]]) and (p_dic[s[i]] > 0):
            char_count += 1

        if char_count == len(p):

            while (s_dic[s[i]] > p_dic[s[i]]) or (p_dic[s[i]] == 0): ####
                if s_dic[s[i]] > p_dic[s[i]]:
                    s_dic[s[i]] -= 1

            start += 1

        len_window = i - start + 1
        if (min_len > len_window):
            min_len = len_window
            start_index = start

    if start_index == -1:
        return None

    return s[start_index:(start_index + min_len)]



