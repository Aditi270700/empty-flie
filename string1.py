# replace (old_value,new_value) it is for changing the world
s = "we are here to learn c++ ,it is a high lang"
s1 = s.replace("c++","python")
s2 = s.replace('a','b',1) # 1 is used is only 1 place change
s3 = s.replace(s,"new")
print(s1,s2)
print(s3)

# split() --> return list
r = "we are here to learn c++ it is here a lang"
r1 = r.split()
print(r1)
r1 =r.split('a')
print(r1)
r1=r.split("here",1)
print(r1)

# join() ---> return string

lis = ["apple","banana","pineapple","orange"]
lis2 = ["pppp","gdhg"]
s=" ".join(lis)+"    "+" ".join(lis2)
print(s)
# slice , split,join
s="its not or never"
#"sti.won.ro.reven"
s = s.split()
print(s)#['its', 'not', 'or', 'never']
a=s[0][::-1]
b=s[1][::-1]
c=s[2][::-1]
d=s[3][::-1]
s=[a,b,c,d]
print(s)


s = "Apple Banana"
a = s[6:]
print(a)
b = s[::-1]
print(b)
c = s[6:]+" "+[:5]
print(c)
