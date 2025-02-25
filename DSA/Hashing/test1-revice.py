# # # # # # l = [1,2,3,1,3,2,2,2,2,2,4,2,5,4,6,5,7,45,7,8]
# # # # # # n = len(l)
# # # # # # hasher = {}
# # # # # # print(type(hasher))

# # # # # # for i,v in enumerate(l):
# # # # # #     if v not in hasher:
# # # # # #         hasher[v] = 1
# # # # # #     else:
# # # # # #         hasher[v] += 1
# # # # # # print(hasher)
# # # # # # temp = 0
# # # # # # for i in hasher:
# # # # # #     if temp < hasher[i]:
# # # # # #         temp = hasher[i]
# # # # # # print(temp)
# # # # # # if temp in hasher:
# # # # # #     print(hasher.keys())

# # # # # # for keys,value in hasher.items():
# # # # # #     if value == temp:
# # # # # #         print(keys)
        
        

# # # # # # s = ["he","bolo","helo","tata","bolo","check"]
# # # # # s= [3,2,3]
# # # # # h = {}
# # # # # for v in s:
# # # # #     if v not in h:
# # # # #         h[v] = 1
# # # # #     else:
# # # # #         h[v] +=1
# # # # # max_frq = max(h.values())
# # # # # # mk = [k for k,v in h.items() if v == max_frq]
# # # # # for k in h:
# # # # #     if h[k] == max_frq:
# # # # #         break
# # # # # print(k)



# # # # s = "abcabcbb"
# # # # n = len(s)
# # # # d = {}

# # # # for i in range(n):
# # # #     print(s[i])
# # # #     if s[i] not in d:  # Initialize list if key doesn't exist
# # # #         d[s[i]] = []
# # # #     d[s[i]].append(i)  # Append the index

# # # # print(d)

# # # # # s = "abcabcbb"
# # # # s = "abca"
# # # # n=len(s)
# # # # d = {}
# # # # i=0
# # # # while i < n:
# # # # # for i in  range(n):
# # # #     if s[i] not in d[i]:
# # # #         d[i]= []
# # # #     d[i].append(s[i])
# # # # print(d)



# # # # s = "swiss"
# # # # char_freq = {}

# # # # # Build frequency dictionary
# # # # for char in s:
# # # #     char_freq[char] = char_freq.get(char, 0) + 1

# # # # # Find the most frequent character
# # # # max_count = 0
# # # # most_frequent_char = ''

# # # # for char, count in char_freq.items():
# # # #     if count > max_count:
# # # #         max_count = count
# # # #         most_frequent_char = char

# # # # print(most_frequent_char)


# # # s1 = "listen"
# # # s2 = "silent"
# # # frq_char={}
# # # for i in range(len(s1)):
# # #     if s1[i] not in frq_char:
# # #         frq_char[s1[i]] = 1
# # #     else:
# # #         frq_char[s1[i]] += 1
# # #     if s2[i] not in frq_char:
# # #         frq_char[s2[i]] = 1
# # #     else:
# # #         frq_char[s2[i]] += 1
# # # print(frq_char)


# # l = [1,2,4,5]
# # a = l[0]
# # res = 0
# # for i in range(1,len(l)):
# #     if l[i] != a + 1:
# #         res = l[i] - 1
# #         a = l[i]
# #     a = l[i]
    
# # print(res)


# arr = [1, 2, 3, 1, 2, 1]
# index_map = {}  # Dictionary to store indices

# for i, num in enumerate(arr):
#     if num not in index_map:
#         index_map[num] = []  # Initialize list for first occurrence
#     index_map[num].append(i)  # Append index to the list

# print(index_map) 
# # Output: {1: [0, 3, 5], 2: [1, 4], 3: [2]}


# ha[num].append(i)





# s1 = "abcd"
# s2 = "abcde"

# dif_map={}

# for v in s2:
#     dif_map[v] = dif_map.get(v,0) + 1
    
# for ch in s1:
#     if ch in dif_map:
#         dif_map[ch] -= 1
# print(dif_map)
# res = [key for key,value in dif_map.items() if value > 0][0]
# print(res)



# li = [11,1,3,5,7,9]   # k <= 10  # sub-array ####### longest sub-array

# max_sub_li, sums, left, right = 0, 0, 0, 0
# k = 10
# res_index =[]
# while right < len(li):
#     sums = sums + li[right]
#     if sums > k:
#         sums = sums - li[left]
#         left += 1
#     if sums <= k:
#         max_sub_li = max(max_sub_li, right - left + 1)
#         res_index = [index for index in range(left,right+1,1)]
#     right += 1
# print(max_sub_li)
# print(res_index)



# def remove_duplicates(arr):
#     if not arr:
#         return 0
    
#     left = 0  # Slow pointer

#     for right in range(1, len(arr)):  # Fast pointer
#         if arr[right] != arr[left]:
#             left += 1
#             arr[left] = arr[right]  # Overwrite duplicate valuesarr.
#     print(arr)
#     return arr[:left + 1]  # Return the modified array (up to unique values)

# # Example Usage
# arr = [1,2, 2, 3, 3,3,3,3,3,3,3,3, 4]
# print(remove_duplicates(arr))  # Output: [1, 2, 3, 4]



# 2️⃣ Remove Duplicates from Sorted Array (Easy)
# Problem: Given a sorted array, remove duplicates in-place without extra space.
# Example:
# arr = [1, 1, 2, 3, 3, 4]  
# Output: [1, 2, 3, 4] (Modify input array)
# ✅ Hint: Use slow and fast pointers.

# arr = [1,1,1,1,1, 1, 2, 3, 3, 4,4,4,4,4,4,4]
# count,left = 0,0
# for right in range(1,len(arr)-1):
#     if arr[left] == arr[right]:
#         arr[right] = arr[right]+1
#     elif arr[left] > arr[right]:
#         arr[left] = arr[right]
#     else:
#         left +=1
# print(left)
# print(arr[:left])

# 5️⃣ Three Sum (Medium)
# Problem: Find all unique triplets (a, b, c) where a + b + c = 0.
# Example:
# nums = [-1, 0, 1, 2, -1, -4]  
# Output: [[-1, -1, 2], [-1, 0, 1]]
# ✅ Hint: Sort and use two pointers inside a loop.

nums = [-1, 0, 1, 2, -1, -4]
nums.sort()  # Sorting is important to avoid duplicates
n = len(nums)
res = []

for i in range(n):
    if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements for 'i'
        continue
    left, right = i + 1, n - 1  # Two-pointer setup
    
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        
        if total == 0:
            res.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:  # Skip duplicate 'left' values
                left += 1
            while left < right and nums[right] == nums[right + 1]:  # Skip duplicate 'right' values
                right -= 1
        elif total < 0:
            left += 1  # Move left pointer to increase sum
        else:
            right -= 1  # Move right pointer to decrease sum

print(res)



left ,right = -1,1
count,max = 0,0
while right < len(max_frq):
    left += 1
    for i in range(max_frq[right],max_frq[left],-1):
        # print(heights[i])
        if heights[i] < heights[max_frq[left+1]]:
            # print(heights[i], "<", heights[left+1])
            count = count + heights[max_frq[left+1]] - heights[i]
            # print(count)
#         if heights[i] <= heights[max_frq[left]+1]:
#             # print(i, heights[i])
#             count = count + heights[max_frq[left]] - heights[i]
            print("max_frq",[left],max_frq[left],"max_frq[right]",max_frq[right]," iam i",i, " heights[i]",heights[i],"[left+1]",left+1 ,"i am count  = ",heights[max_frq[left+1]] ,"-", heights[i], count)
    right +=1
print(count)