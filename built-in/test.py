# l= [1,2,3,-4,-5,-6,-7,-8]
# lm=[abs(i) for i in l]
# print(lm)
# listsame=[1,1,1]
# listdiff=[1,2,3]
# all(x==1 for x in listsame)
# all(x ==1 for x in listdiff)
# any(x==1 for x in listdiff)
# any(x==3 for x in listsame)

# x = 10
# y = 'Hi'
# z = 'Hello'
# print(y)

# breakpoint()

# print(z)


# for i in range(10):
#     print("i=",i)
    
#     if i ==5:
#         #import pdb; pdb.set_trace()
#         breakpoint()

def average(iplist):
    return (sum(iplist)/len(iplist))
#input call function
iplist=[10,20,30,40]
print(average(iplist))


l=[1,2,3,4,5]
print(sum(l))