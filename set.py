# set:
# set is a container in which we contain multiple data, but 
# duplication is not allowed, and unordered datatype
# where our main concern is data, but not any order related to it,
# then we use set.
# collection of alphabet ---> super set
# a,e,i,o,u ----> subset

# A = {1,3,9,9,7,2,5}
# B = {2,3,99,11,99,5}
# A intersection B ---> {3,2,5}
# A union B ---> {1,7,9,3,2,5,99,11}
# A-B ---> {1,7,9}
# B-A ---> {99,11}
# intersection means common 
# union means both set
s1 = {1,2,3,3,4,9,11,17}
s2 = {4,5,9,17,89}
s3 = {"a","b",1,2,3,88}
print(s1)
r=s1.union(s2)
print(r)
r=s1.intersection(s2)
print(r)
r=s1.union(s2,s3)
print(r)
r=s1.intersection(s2,s3)
print(r)
r = s1.difference(s2)
print(r)
# update in s1
s1.update(s2)
print(s1)
# add take all object
s1.add(99)
print(s1)
# add tuple
s1.add((5,))
print(s1)

# r = s1|s2|s3 ---> union
# r = s1&s2&s3 ---> intersection
# r = s1-s2-s3 ---> difference means ignore common and s2



