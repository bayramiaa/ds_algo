"""
Given an ascending and descending array of distinct integers, find the maxima.

[-4, 2, 3, 6, 3, 1] -> 6
[-4, 5, 10, 11] -> 11
[11, 2, 0] -> 11


[..., 3, 4, 5, ...]

Cases when middle == 0
[1]
[1, 2]


[1, 2, 3]
mid = 2
left = 1
right = 3

first += 1
first = 1
end = 2

(first + end) // 2 = 1

    end = 10k
    mid = 5k
    first += 1
    
    end = 10k
    first = 5k
    middle = 7.5k
    

mid = 2
first += 1
(first + end) // 2 = 2
mid = 3
right = error

"""


def find_maxima(arr):
    first = 0
    end = len(arr) - 1
    found = False
    
    if len(arr) == 1:
        return arr[0]
    
    if len(arr) == 2:
        return max(arr)
    
    while not found:
        middle = (first + end) // 2
        
        if middle == 0 or middle == len(arr) -1:
            return arr[middle]
        
        mid = arr[middle]
        left = arr[middle -1]
        right = arr[middle + 1]
        
        if right > mid:  # [..., 2, <4, ...>]
            first = middle + 1
        if left > mid: # [<..., 4>, 3, ...]
            end  = middle - 1
        if right < mid and left < mid:
            found = True
            
    return arr[middle]



#print find_maxima([-4, 2, 3, 6, 3, 1]) == 6
#print find_maxima([-4, 5, 10, 11]) == 11            


"""
Given an array of strings, find the length of the longest common prefix among all strings. There exists at least one string.

['hiii', 'hi', 'hiiiiiii'] -> 'hi' -> 2
['fooo', 'bar'] -> '' -> 0
['adad', 'dada'] -> '' -> 0
"""


def largest_common_prefix(word_array): #O(nm)
    if len(word_array) == 1:
        return len(word_array[0])
    
    #min_len = get_min_len(word_array)
    
    prefix = ''
    count = 0
    while True: #for i in range(min_len): #O(m)
        letters = [word[count] for word in word_array] #O(n)
        letter_set = set(letters) 
        if len(letter_set) == 1:
            prefix += letter_set.pop()
            count += 1
        else:
            break
    
    return len(prefix)


def get_min_len(word_array): #O(n)
    min_len = float('inf')
    for word in word_array:
        if len(word) < min_len: 
            min_len = len(word)
            
    return min_len

print largest_common_prefix(['hiii', 'hci', 'hiiiiiii']) == 1
print largest_common_prefix(['fooo', 'bar']) == 0
