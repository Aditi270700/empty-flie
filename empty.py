#empty list

#1
lis=[]
#2
li = list() # list method

print(lis)
print(li)
#any()
print(any(lis))#false


lis=[21]
print(any(lis))#true
'''
#append--->
lis = [23,45,6,7,88]
print(lis)
lis.append(10)
print(lis)
lis.append(["mango","banana"])
print(lis)
print(lis[6][0])

#question
lis.append(["mango","banana","apple"])
print(lis)
lis.append(["200kg","50kg","100kg"])
print(lis[6][2])
print(lis[7][2])
'''
lis=[]
print(lis)
lis.append(["mango","banana"])
lis.append(["200kg","50kg"])
lis[0].append("apple")
lis[1].append("300kg")
print(lis)

#extend lis.extend(sequence)

lis.extend(["pineapple","papaya"])
print(lis)

#insert(index,element)
lis.insert(2,"orange")
print(lis)

lis[0]="grapes"
print(lis)

# len() ,max(), min(), sum()
lis1 = [23,4,-5,6,77]
m=max(lis1)
print(m)
v=min(lis1)
print(v)