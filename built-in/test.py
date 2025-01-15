# # l= [1,2,3,-4,-5,-6,-7,-8]
# # lm=[abs(i) for i in l]
# # print(lm)
# # listsame=[1,1,1]
# # listdiff=[1,2,3]
# # all(x==1 for x in listsame)
# # all(x ==1 for x in listdiff)
# # any(x==1 for x in listdiff)
# # any(x==3 for x in listsame)

# # x = 10
# # y = 'Hi'
# # z = 'Hello'
# # print(y)

# # breakpoint()

# # print(z)


# # for i in range(10):
# #     print("i=",i)
    
# #     if i ==5:
# #         #import pdb; pdb.set_trace()
# #         breakpoint()

# def SmallestElement(iplist):
#     x=0
#     for i in range(len(iplist)-1):
#         if iplist[i] < iplist[i +1]:
#             x = iplist[i]
#         else:
#             x = iplist[i +1]
#     return x

# iplist=[8,100,20,40,3,7]

# print(SmallestElement(iplist))


# s = "00110011"
s = "010010"
res=0
x=[]
y=[]
count = 0
print("len(s)", len(s))
for i in range(len(s)-1):
    if s[i+1]!=s[i]:
        res=res+1
    if s[i] == "0":
        x.append(i)
    else:
        y.append(i)

print(s[-1])
if s[-1]==1:
    y.append(len(s)-1)
    print(" iam x from if ",y)
else:
    x.append(len(s)-1)
    print(" iam from Y",x)
    
print(x,y,res)
while count < len(s)-1:
    test=0
    if count < len(x)-1:
        test = x[count+1] - x[count]
        if test -2 == 1:
            res = res + test - 2
    if count < len(y)-1:
        test = y[count+1]-y[count]
        if test -2 == 1:
            res = res + test - 2
    count = count +1 

print(res)

if x[-1]-x[-2]==1 and x[-1]==len(s)-3:
    print("  am i working")
    res = res + 1
print( res)