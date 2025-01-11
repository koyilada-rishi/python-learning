ab=abs(-1)
#it gives all the absoulute values
all=all([])
#can help in checking empty or not ( default True )
any=any([])
# can check for empty ( default false )
print(ab,"         I am abs\n", all, "      I am from All \n", any, "       I am from Any \n")

buitin = dir(__builtins__)
# will give you all built-in functions
print(buitin)

built_abs=dir(abs)
# will give all built in methods of abs builtin function
print(built_abs)

l= [1,2,3,-4,-5,-6,-7,-8]
lm=[abs(i) for i in l]
print(lm)

listsame=[1,1,1]
listdiff=[1,2,3]
all(x==1 for x in listsame)
all(x ==1 for x in listdiff)
any(x==1 for x in listdiff)
any(x==3 for x in listsame)