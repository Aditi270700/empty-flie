# it is a mapping datatype in which each element is represeted as key value pair
# it is mutable data type
# it is a ordered data type
# element first inserted 
# if we iterate a dictionary using for loop then data must be fetched in the order, in 
#which it has been inserted
# reresentation of dictionary
# {} is used in set and dictionary

d={"one":"monday","two":"tuesday","three":"wednesday,one:jan"}
print(d)
print(d["two"])
d["four"]="thursday"
d["five"]="friday"
d["one"]="friday"
d.update({"six":"saturday"})
d1={"seven":"sunday"}
print(d,d1)
'''
property of key:
1) key should be .new key-value pair overwrite old key-value 
2) key must be consist of inmutable datatype
3) 
property of value:
1) value can be duplicated
2) value can be consist of datatype
'''


