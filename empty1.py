lis=[]#method1
li=list()
print (lis)
print(li)


# any
print(any(lis)) #false

lis=[21]
print(any(lis))

#lis.append
lis=[]
print(lis)
lis.append(["mango","banana"])
lis.append(["200kg","300kg"])
lis[0].append("apple")
lis[1].append("500kg")
lis[0].append("orange")
lis[1].append("100kg")
print(lis)

# lis.extend
lis.extend(["papaya","gavava"])
print(lis)

 # lis.insert
lis.insert(0,"pineapple")
print(lis)

lis.insert(1,"stawberry")
print(lis)
