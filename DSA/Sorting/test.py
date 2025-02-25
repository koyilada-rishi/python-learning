# def Bubble_Sort(l):
#     n = len(l)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if l[j] > l[j+1]:
#                 l[j],l[j+1] = l[j+1],l[j]
#     return l

# l=[1,4,6,2,3,8]

# print(Bubble_Sort(l))



# def Selection_Sort(l):
#     n = len(l)
#     for i in range(n-1):
#         min = i  # Store the index of the smallest element
#         for j in range(i+1, n):  # Look for a smaller element in the remaining array
#             if l[min] > l[j]:  # If a smaller element is found, update min index
#                 min = j
#         # Swap only once per iteration
#         l[i], l[min] = l[min], l[i]
#     return l

# l=[1,4,6,2,3,8]
# print(Selection_Sort(l))



# # Merge two sorted arrays
# def merge_array(a,b):
#     res = []
#     j=0
#     c=1
#     for i in range(len(a)):
#         while  j < len(b) :
#             if a[i] > b[j]:
#                 res.append(b[j])
#                 j = j+1
#             elif a[i] < b[j]:
#                 if i == len(a)-1 and res[len(res)-c] == a[i-1]: # last second values i am checking and then appending it
#                     if c == 1:
#                         res.append(a[i])
#                         c = c + 1
#                     res.append(b[j])
#                     if j != len(b)-1:
#                         j = j+ 1
#                         c = c + 1
#                     else:
#                         break
#                 else:
#                     res.append(a[i])
#                     break
#         if j == len(b): # this is written cause if a len is more that b so b(j) will be done with while loop so rest of  the a values which are sorted one will be appended 
#             res.append(a[i])

#     print(res)
    

# # a = [10,15]
# # b = [5,6,6,30,40]
# a = [1,3,5,7,9,10]
# b = [2,4,6,8]

# # merge_array(a,b)






# def merge_subarray(l,low,mid,high):
#     j = 0
#     a=[]
#     b=[]
#     m=len(a)
#     n=len(b)
#     if low < mid < high:
#         while j < mid + 1 :
#             a.append(l[j])
#             j = j + 1
#         print(" iam j", j)
#         while j < high + 1:
#             b.append(l[j])
#             j = j + 1
#     print(a,b)

# l=[10,15,20,11,13]
# low = 0
# high = 4
# mid = 2
# merge_subarray(l,low,mid,high)




# # Merge sub arrays ex:  I/P a = [10,15,20,11,13] ; low = 0 ; high = 4 ; mid = 2
# # create two arrays between low to mid and mid to high
# # compare and merge those two sorted arrays

# # splitting  a and b arrays using low , mid , high and using ma_s() for sort array return
# def merge(arr,low,mid,high):
#     left = arr[low:mid+1]
#     right = arr[mid+1:high+1]
#     i,j = 0,0
#     k = low
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             arr[k] = left[i]
#             k = k + 1
#             i = i + 1
#         else:
#             arr[k] = right[j]
#             k = k + 1
#             j = j + 1
#     while i < len(left):
#             arr[k] = left[i]
#             k = k + 1
#             i = i + 1
#     while j < len(right):
#             arr[k] = right[j]
#             k = k + 1
#             j = j + 1

# def merge_sort(arr,low,high):
#     if high > low :
#         mid = (high + low)//2
#         merge_sort(arr,low,mid)
#         merge_sort(arr,mid+1,high)
#         merge(arr,low,mid,high)

# arr = [10,15,20,40,8,11,55]
# low = 0
# high = 6

# merge_sort(arr,low,high)
# print(arr)
# l=[10,15,20,11,13]
# low = 0
# high = 4
# mid = 2

# l = [10,15,20,40,8,11,55]
# low = 0
# mid = 3
# high = 6

# merge(l,low,mid,high)
# print(l)


# import json

# # Define the path to your JSON file
# json_file_path = "top.json"  # Change this to your actual path

# # Read JSON file
# with open(json_file_path, "r") as file:
#     data = json.load(file)

# # Print the count of items in the JSON file
# print("Total Count:", type(data), len(data))

# # print(data[0]["PID"]) 

# for i in range(len(data)):
#     print(data[i]["VIRT"])
# print("I am count in total", i)

# print(type(data),data[0])





import json

def bubble_sort(data):
    # Creating a copy of the input data to avoid modifying the original data
    res = data[:]
    n = len(res)
    
    # Bubble Sort Logic: Iterate over the data and sort by "VIRT"
    for i in range(n-1):
        for j in range(n-i-1):
            # Comparing "VIRT" values
            if res[j]["VIRT"] > res[j+1]["VIRT"]:
                res[j], res[j+1] = res[j+1], res[j]
    
    return res

# Define the path to your JSON file
json_file_path = "top.json"  # Change this to your actual path

# Read the JSON file
with open(json_file_path, "r") as file:
    data = json.load(file)

# Print the sorted data
sorted_data = bubble_sort(data)
print(sorted_data)


# import json

# def bubble_sort(data):
#     # Creating a copy of the input data to avoid modifying the original data
#     res = data[:]
#     n = len(res)
    
#     # Bubble Sort Logic: Iterate over the data and sort by "VIRT"
#     for i in range(n-1):
#         for j in range(n-i-1):
#             # Get the VIRT values, default to 0 if None
#             virt_j = res[j].get("VIRT", 0) if res[j].get("VIRT") is not None else 0
#             virt_jp1 = res[j+1].get("VIRT", 0) if res[j+1].get("VIRT") is not None else 0
            
#             # Compare the values, considering defaulting to 0 for None values
#             if float(virt_j) > float(virt_jp1):  # Ensure the comparison is numeric
#                 res[j], res[j+1] = res[j+1], res[j]
    
#     return res

# # Define the path to your JSON file
# json_file_path = "top.json"  # Change this to your actual path

# # Read the JSON file
# with open(json_file_path, "r") as file:
#     data = json.load(file)

# # Print the sorted data
# sorted_data = bubble_sort(data)
# print(sorted_data)
