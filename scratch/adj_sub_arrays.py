arr = [5,  5, 10, 40, 50, 35]
def find_max_sum(arr):
    incl = 0
    excl = 0
    
    for i in arr:
         
        # Current max excluding i (No ternary in 
        # Python)
        new_excl = max(incl, excl)
        
        # Current max including i
        incl = excl + i
        excl = new_excl
     
    # return max of incl and excl
    return max(excl, incl)

find_max_sum(arr)