##ref:- https://github/koyilada-rishi/python-learning/blob/main/python-learning/DSA/Two-Pointer_Sliding-window/gpt-15.ipynb#C6:L4-L5


## Stage One

## print a list 
test_list = list(range(1,10))
print(test_list)


#### new concepts from  same ref as above

def missing_nums(arr):
    arr=set(arr)
    n = len(arr)
    full_list=set(range(1,n+1))  #### new concept
    missing_nums_res = list(full_list - arr)  #### new concept
    print(missing_nums_res)
missing_nums([2, 3, 4, 6, 7])



