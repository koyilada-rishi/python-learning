l= [1,2,3,-4,-5,-6,-7,-8]
lm=[abs(i) for i in l]
print(lm)
listsame=[1,1,1]
listdiff=[1,2,3]
all(x==1 for x in listsame)
all(x ==1 for x in listdiff)
any(x==1 for x in listdiff)
any(x==3 for x in listsame)