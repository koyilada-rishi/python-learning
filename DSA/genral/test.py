# # * * * * * * * * * * * 
# # *                   * 
# # *                   * 
# # *                   * 
# # * * * * * * * * * * * 
# # for this code i took a technique like print(0 and 4 rows first and next worked on columns printing)
# print("\n")
# r=5
# c=15

# for i in range(r):
#     for j in range(c):
#         if (i == 0 or i == r-1 ) or (j == 0 or j == c-1): 
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#         # if (j == 0 or j == c-1):
#         #     print(i,j," ",end="")
#     print()

# #           * * * * * * 
# #         * * * * * * 
# #       * * * * * * 
# #     * * * * * * 
# #   * * * * * * 
# # * * * * * * 


# r =s= 8

# z= (r-1)+s
# t=0
# while z > (r-1):
#     t=t+1
#     for i in range(z):
#         if i < r-t:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()
#     z=z-1
    
    
# sr=3
# ll=5
# z= sr+ll
# while ll > -1:
#     for i in range(z):
#         if i < ll:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     z=z-1
#     ll=ll-1
#     print()
    
# sr=3
# ll=5
# z= sr+ll
# t=0
# while ll > -1:
#     for i in range(z):
#         if i >= t:
#             if i < sr:
#                 print("*", end=" ")
#         else:
#                 print(" ",end=" ")
#     t = t+1
#     z = z+1
#     ll = ll-1
#     sr = sr+1
#     print()





# li=hi=di=0
# for i in range(len(prices)):
#     if prices[i]<prices[li]:
#         li = i
#         if li > hi:
#             hi = i
#     if prices[i] > prices[hi]:
#         hi = i
#     if prices[hi] - prices[li] > di:
#         di = prices[hi] - prices[li]
# print( di)

# prices = [2,1,4,1,10,1,0,4]
# lowestPrice = float("inf")
# profit = 0

# for i in prices:
#     if i < lowestPrice:
#         lowestPrice = i
#     elif i - lowestPrice > profit:
#         profit = i - lowestPrice

# print(profit)

# n = 10

# for _ in range(n):
#     if i >= n:
#         break
#     print(i)
#     i *= 2


# # nums = [7,1,5,4]
# # nums =[9,4,3,2]
# # nums = [1,5,2,10]
# nums = [7,1,5,4]
# # nums =[9,4,3,2]
# # nums = [1,5,2,10]
# nums= [2543,291,105,1118,1615,3713,3618,3454,2731,4173,579,2133,2575,616,1936,924,2870,2524,2203,3428,160,239,2869,1526,1228,3461,4182,1834,1785,2414,3553,1064,1842,1823,2826,47,458,837,75,2986,2871,1558,3238,114,144,1699,170,3551,1125,2531,1110,721,2505,2422,2166,2621,3436,412,3182,2718,569,19,2707,3561,3842,3112,833,2646,2095,378,3838,633,1404,3359,1375,686,3880,2527,637,2063,1201,3558,4108,1470,3610,1440,722,2519,1280,2985,3591,2939,1273,1564,353,1339,1148,3159,2261,1611,2689,315,3429,1710,714,1028,1287,815,1041,1760,1518,199,148,3071,4207,1279,2802,2385,1436,1120,2934,4070,3437,473,2107,1885,2474,2005,2889,3376,422,2580,3180,416,3508,877,322,3931,1060,1582,3712,632,180,3865,1342,1779,2912,3338,2808,1776,342,4175,2470,692,1993,2003,1137,1431,1578,4135,2460,194,1837,3077,471,4025,1409,3120,2368,2849,4229,1645,3699,2435,3453,2333,3983,1154,3253,97,2251,3867,3663,1031,1845,1912,3061,2338,1527,3608,1675,3950,2118,3619,3349,2638,964,1857,3791,1716,4103,3210,3629,3243,394,1597,779,165,4056,2731,6,1506,4133,753,3204,2685,2804,3020,3738,3897,1404,4141,1707,2511,3309,3681,813,433,1537,980,3524,2195,1943,1355,813,297,4109,1209,2572,3454,697,579,202,1150,3210,3917,3794,2323,1035,289,2214,2720,2666,3269,3821,2478,1442,3052,2094,1821,3947,2667,2463,2341,2009,1724,3359,3818,3378,2719,1499,1769,3569,670,3402,1174,3968,1273,2655,85,2862,2599,871,1751,1307,3311,1012,2161,1898,738,2056,1417,1864,1883,1508,778,4099,3018,1719,231,552,486,2427,2144,2232,2331,3652,1956,980,1339,1200,2477,2736,1141,3993,398,650,3291,3877,3248,1617,2847,2582,4022,1977,834,2353,324,1345,877,2104,3334,1019,4088,3289,1966,2322,3545,1830,2481,1741,419,2741,2899,4172,2369,1131,3146,152,2284,3081,3238,212,1865,1507,3640,1269,1974,453,4105,3363,1466,694,379,2378,1820,1948,1929,2279,1886,1699,2997,3960,3823,545,2064,114,1456,3342,2367,3769,780,2981,2184,546,3072,432,3458,2468,997,356,3197,2169,3436,1887,2095,3756,15,3304,1592,3761,1306,1581,96,1531,301,493,601,2119,2605,960,2284,2554,1005,2266,2208,3319,1888,3734,281,3760,1286,3575]
# t=0
# # res= -float("inf")
# res = -1
# for i in range(len(nums)-1):
#     j= i+1
#     print(f" we are intitialize i , j {i} , {j}")
#     if nums[i] < nums[j]:
#         print(f" nums[i] < nums[j] {nums[i] < nums[j]}")
#         if (res < nums[j] - nums[i]):
#             print(f" if res < nums[j] - nums[i] {res < nums[j] - nums[i]}")
#             if (nums[j] - nums[i]) < (nums[j] - nums[t]):
#                 res = nums[j] - nums[t]
#             else:
#                 res = nums[j] - nums[i]
#                 print(f"iam from result res  {res}")
#                 t = i
#             print(f" iam t values {t}")
#         elif nums[j] - nums[t] > res:
#             res = nums[j] - nums[t]
#             print(f"i am  nums[j] - nums[t] > res  {nums[j] - - nums[t] > res}   res = {res}")
# print(res)


# # nums = [2543, 291, 105, 1118, 1615, 3713, 3618, 3454, 2731, 4173, 579, 2133, 2575, 616, 1936, 924, 2870, 2524, 2203, 3428, 160, 239, 2869, 1526, 1228, 3461, 4182, 1834, 1785, 2414, 3553, 1064, 1842, 1823, 2826, 47, 458, 837, 75, 2986, 2871, 1558, 3238, 114, 144, 1699, 170, 3551, 1125, 2531, 1110, 721, 2505, 2422, 2166, 2621, 3436, 412, 3182, 2718, 569, 19, 2707, 3561, 3842, 3112, 833, 2646, 2095, 378, 3838, 633, 1404, 3359, 1375, 686, 3880, 2527, 637, 2063, 1201, 3558, 4108, 1470, 3610, 1440, 722, 2519, 1280, 2985, 3591, 2939, 1273, 1564, 353, 1339, 1148, 3159, 2261, 1611, 2689, 315, 3429, 1710, 714, 1028, 1287, 815, 1041, 1760, 1518, 199, 148, 3071, 4207, 1279, 2802, 2385, 1436, 1120, 2934, 4070, 3437, 473, 2107, 1885, 2474, 2005, 2889, 3376, 422, 2580, 3180, 416, 3508, 877, 322, 3931, 1060, 1582, 3712, 632, 180, 3865, 1342, 1779, 2912, 3338, 2808, 1776, 342, 4175, 2470, 692, 1993, 2003, 1137, 1431, 1578, 4135, 2460, 194, 1837, 3077, 471, 4025, 1409, 3120, 2368, 2849, 4229, 1645, 3699, 2435, 3453, 2333, 3983, 1154, 3253, 97, 2251, 3867, 3663, 1031, 1845, 1912, 3061, 2338, 1527, 3608, 1675, 3950, 2118, 3619, 3349, 2638, 964, 1857, 3791, 1716, 4103, 3210, 3629, 3243, 394, 1597, 779, 165, 4056, 2731, 6, 1506, 4133, 753, 3204, 2685, 2804, 3020, 3738, 3897, 1404, 4141, 1707, 2511, 3309, 3681, 813, 433, 1537, 980, 3524, 2195, 1943, 1355, 813, 297, 4109, 1209, 2572, 3454, 697, 579, 202, 1150, 3210, 3917, 3794, 2323, 1035, 289, 2214, 2720, 2666, 3269, 3821, 2478, 1442, 3052, 2094, 1821, 3947, 2667, 2463, 2341, 2009, 1724, 3359, 3818, 3378, 2719, 1499, 1769, 3569, 670, 3402, 1174, 3968, 1273, 2655, 85, 2862, 2599, 871, 1751, 1307, 3311, 1012, 2161, 1898, 738, 2056, 1417, 1864, 1883, 1508, 778, 4099, 3018, 1719, 231, 552, 486, 2427, 2144, 2232, 2331, 3652, 1956, 980, 1339, 1200, 2477, 2736, 1141, 3993, 398, 650, 3291, 3877, 3248, 1617, 2847, 2582, 4022, 1977, 834, 2353, 324, 1345, 877, 2104, 3334, 1019, 4088, 3289, 1966, 2322, 3545, 1830, 2481, 1741, 419, 2741, 2899, 4172, 2369, 1131, 3146, 152, 2284, 3081, 3238, 212, 1865, 1507, 3640, 1269, 1974, 453, 4105, 3363, 1466, 694, 379, 2378, 1820, 1948, 1929, 2279, 1886, 1699, 2997, 3960, 3823, 545, 2064, 114, 1456, 3342, 2367, 3769, 780, 2981, 2184, 546, 3072, 432, 3458, 2468, 997, 356, 3197, 2169, 3436, 1887, 2095, 3756, 15, 3304, 1592, 3761, 1306, 1581, 96, 1531, 301, 493, 601, 2119, 2605, 960, 2284, 2554, 1005, 2266, 2208, 3319, 1888, 3734, 281, 3760, 1286, 3575]
# # # nums = [7,1,5,4]
# # # nums =[9,4,3,2]
# # # nums = [1,5,2,10]
# # # nums = [7,1,5,4]
# # # nums =[9,4,3,2]
# # # nums = [1,5,2,10]
# # t = 0  # Track the index of the smallest number
# # res = -float("inf")  # Track the maximum profit (or difference)

# # for i in range(1, len(nums)):
# #     if nums[i] - nums[t] > res:
# #         res = nums[i] - nums[t]  # Update the maximum profit
# #     if nums[i] < nums[t]:
# #         t = i  # Update the index of the smallest number

# # print(res)  # Output: 4210
# li = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 
# print (li[0][-1])

# a = ['Learn', 'Quiz', 'Practice', 'Contribute'] 
# b = a 
# print(f"finding a  a in {a}")
# print(f"finding b  b in {b}") 
# c = a[:] 

# b[0] = 'Code'
# b.append('rishi')
# print(f"finding b  a in {a}")
# print(f"finding b  b in {b}") 
# c[1] = 'Mcq'
# print(f"finding * a in {a}")

# print(f"finding * b in {b}")

# print(f"fining  * c in {c}")
# count = 0
# for c in (a, b, c): 
#   print(c)
#   if c[0] == 'Code': 
#     count += 1
#   if c[1] == 'Mcq': 
#     count += 10

# print (count)



# def fun1():
#     print("fun1() called")
# def fun2():
#     print("Before fun1()")
#     fun1()
#     print("After fun1()")

# print("Before fun2()")
# fun2()
# print("After fun2()")


# def fun(n):
#     if n==0:
#         return 
#     print("GFG")
#     fun(n-1)

# fun(3)

# def fun(n):
#     if n == 0:
#         return
#     print(n/2)
#     fun(n/2)
#     # print(n % 2)
    
# fun(13)




#####      binary search 1st Occurance
def se(li,x):
    low = 0
    high = len(li)-1
    while low <= high:
        mid = (low + high)//2
        if x > li[mid]:
            low = mid + 1
        elif x < li[mid]:
            high = mid - 1
        elif mid == 0 or li[mid-1] != x:
            return mid
        else:
            high = mid - 1
        
    return -1 

li = [2,3,5,5,5,5,9,9,9,11]
x = 9
print(se(li,x))


##### Binary Search last Occurance\\

def sel(li,x):
    low = 0
    high = len(li)-1
    while low <= high:
        mid = (low + high)//2
        if x > li[mid]:
            low = mid + 1
        elif x < li[mid]:
            high = mid - 1
        elif mid == high or li[mid+1] != x:
            return mid
        else:
            low = mid + 1
        
    return -1 

li = [2,2,2,2,4,4,4,4,4,4,4,4,4,4,5,5,9,9,9,11]
x = 2
print(sel(li,x))




####sqaure root

def sq(n):
    low =1
    high = n//2
    ans = -1
    while low <= high:
        mid = (low + high)//2
        sq = mid*mid
        if sq == n:
            return mid
        elif sq > n:
            high = mid -1
        else:
            low = mid + 1 
            ans = mid
    return ans
v
print(sq(4))


class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)  # Manually calling the parent class constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."







# Creating an instance of Dog
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Output: Buddy barks.
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Using super() to call the parent class constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."

# Creating an instance of Dog
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Output: Buddy barks.
