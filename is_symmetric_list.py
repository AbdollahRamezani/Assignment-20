def is_symmetric(lst): 
    if len(lst) == 0: 
        return True 
    for i in range(len(lst)//2): 
        if lst[i] != lst[len(lst)-i-1]: 
            return print("No") 
    return print("Yes")

lst = [2, 3, 5, 3, 2]
is_symmetric(lst)
