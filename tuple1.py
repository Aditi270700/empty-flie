number = (12,99) + (78,90)
number = number + (89,90)
print(number)#(12,90,78,90,89,90)answer

'''
tuple ojject
1 (12,90)
2 (78,90)
3 (12,90,78,90)
4 (89,90)
'''
#           0             1
lis = [["ajay","aman"],(45,67)]
#           0    1       0  1
'''
lis[1][0] = 99#---> (error tuple)
lis.pop()
print(lis)
'''

t = (34,55,[3,2,5555])
print(t)
t[2][2]=23
print(t)

lis = [["ajay","aman"],(45,[67,44])]
# lis[1][1][0]=9999
# print(lis)
print(type(lis[1]))
lis[1][1][1]=55
print(lis)


# tuple function

#len() , max(), min(), sum(), index(), count()
# count
t = (9,44,5,9,3,9)
a=t.count(9)
print(a)

# sorted()----->return sorted list
u = (9,44,5,9,3,9)
a=sorted(u)
print(a)