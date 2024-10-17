st="we are here to learn python and slicing is very helpful"
print(st)
a=st[7:20]
print(a)
a=st[32:]
print(a)
a=st[3:19:3]
print(a)
print(st[:21]+"cpp"+st[27:])

# list,set,dictionary are mutable datatype 

#string 
# 1) sequence (ordered)
# 2) immutable

msg = "string is a immutable data-type"
#msg[3]="y"
print(msg[12:31])

msg = "apple is good 4 health"
# capitalize
print(msg.capitalize()) # two types are capitalize
a=msg.capitalize()
print(a)
b=msg.upper()
print(b)

a=msg.isupper()
print(a)
a=msg.islower()
print(a)
#lower() all letter are convert into small letter
data="ASDFDGDFGFHGJHKJKJ"
c=data.lower()
print(c)