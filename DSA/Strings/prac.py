# # # s1 = "listen"
# # # s2 = "silent"

# # s1 = "abba"
# # s2 = "baba"
# # def anagram_string(s1,s2):
# #     if len(s2) != len(s1):
# #         return False
# #     else:
# #         count = []
# #         i , j = 0 , 0
# #         while j < len(s2):
# #             if i == len(s1) and len(count) == 0:
# #                 break
# #             elif i == len(s1):
# #                 i = 0
# #             elif len(count) == len(s2):
# #                 break
# #             elif i in count:
# #                 i = i + 1 
# #             elif s1[i] == s2[j]:
# #                 count.append(i)
# #                 i = 0
# #                 j = j + 1
# #             else:
# #                 i = i + 1
# #         return True if j == len(s2) else False


# # # Test cases
# # # print(anagram_string("listen", "silent"))  # ✅ True
# # # print(anagram_string("abaa", "aaab"))      # ✅ True
# # # print(anagram_string("test", "sett"))      # ✅ True
# # # print(anagram_string("hello", "world"))    # ❌ False
# # # print(anagram_string("abc", "abcd"))       # ❌ False
# # # print(anagram_string("race", "care"))      # ✅ True
# # # print(anagram_string("aabb", "abab")) 
# # print(anagram_string("aabb", "abbb"))

# # l = [1,8,9]
# # j = 0
# # for i in range(len(l)):
# #     for j in range (i,len(l)):
# #         if l[i] == l[j]:
# #             print(l[j])
# #         else:
# #             print(l[i],l[j])



# # l = [1,8,9]
# # i, j = 0 , 0
# # while i < len(l):
# #     if j < len(l):
# #         if l[i] == l[j]:
# #             print(l[j])
# #         else:
# #             print(l[i],l[j])
# #         j = j + 1
# #     else:
# #         i = i + 1
#         # j = i

# # l = [1,8,9]
# l = "rishi"
# n = len(l)
# j,i = 1,0
# res = []
# while i < n + 2 and j < n:
#     if i == n + 1 :
#         j = j + 1
#         i = j
#     res.append(l[j-1:i])
#     i = i + 1
# print(f" total sub-strings are {len(res)}, list is {res}")


# l = [5,9,1,8,7,8,2,4,5]
# sub_array_len = 3
# n = len(l) - sub_array_len
# total = 0
# index  = []
# print(" iam with  n ",n)
# for i in range(0,n+1,1):
#     if  total < sum(l[i:sub_array_len+i]):
#         total = sum(l[i:sub_array_len+i])
#         if total == sum(l[i:sub_array_len+i]):
#             index.append(list(range(i, sub_array_len + i)))
#         index[0]= list(range(i, sub_array_len + i))
# print(index)
# print(total, index[0])

l = [5,9,1,8,7,8,2,4,5]
sub_array_len = 3
n = len(l) - sub_array_len
total = 0
index  = [0]
print(" iam with  n ",n)
for i in range(0,n+1,1):
    if  total < sum(l[i:sub_array_len+i]):
        if total == sum(l[i:sub_array_len+i]):
            index.append(list(range(i, sub_array_len + i)))
        total = sum(l[i:sub_array_len+i])
        index[0]= list(range(i, sub_array_len + i))
print(index)
print(total, index[0])
