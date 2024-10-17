t = (23)
print(type(t))
t1 = ("abcd",)
print(type(t))
w = 1,2,3,4,5
print(type(w))

# empty tuple
t = ()

t1 = tuple()
print(t,t1)

record = ("ajay",101,23,9090909090)
record = list(record)
record[3],record[0]=45465464,"ajay singh"
print(record)
record = tuple(record)
print(record)


a = 9
b = 7
a,b = 100,700
print(a,b)
