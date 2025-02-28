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

# write a comment for the above def function
# The function takes a list as input and returns a list of missing numbers from the list. 
# The function uses the set() function to convert the input list to a set. 
# The set() function removes duplicate elements from the list. 
# The function then creates a set of numbers from 1 to n using the set() function and the range() function. 
# The function then calculates the missing numbers by subtracting the input list set from the full list set. 
# The function returns the missing numbers as a list.
list1 = [1, 2, 3, 4, 5]




print("6. **Find Majority Element**")
# - **Explanation:** Find the element that appears more than n/2 times.
# - **Hint:** Use a dictionary to count frequencies or Boyer-Moore Voting Algorithm.
# - **Example 1:**
#     - Input: `[3, 3, 4, 2, 3, 3, 3, 1]`
#     - Output: `3`
# - **Example 2:**
#     - Input: `[2, 2, 1, 2, 3, 2]`
#     - Output: `2`
arr = [3, 3, 4, 2, 3, 3, 3, 1]
def find_majority_element(arr):
        n = len(arr)
        frq_dic = {}
        for i in arr:
            frq_dic[i] = frq_dic.get(i,0) + 1
        for keys,values in frq_dic.items():
            if values >= n//2:
                return keys

# give me all test cases to run the above code


print("9. **Check if Two Arrays are Permutations of Each Other**")
# - **Explanation:** Verify whether two arrays contain the same elements with the same frequencies.
# - **Hint:** Build frequency dictionaries for both and compare.
# - **Example 1:**
#     - Input: `[1,2,3]` and `[3,2,1]`
#     - Output: `True`
# - **Example 2:**
#     - Input: `[1,2,2]` and `[2,1,1]`
#     - Output: `False`

def is_permutation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    frq_dic = {}
    for value in arr1:
        frq_dic[value] = frq_dic.get(value,0) + 1
    for value in arr2:
        frq_dic[value] = frq_dic.get(value,0) - 1
    # return all(value == 0 for key,value in frq_dic.items())
    return all(value == 0 for value in frq_dic.values())

print(is_permutation([1,2,3], [3,2,1]))  # Output: True




