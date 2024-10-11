
nums = [2,43,45,56,7,45,9,-33,44,45,5,6,45,5,6]

# index, index(element,start,end)
# index return index value of element passed, we can give maximum of 3 parameter in index()
# in first parameter, you have to pass the element itself
# and second and third are optional parameter,
# second -->start
# third -->end(excluded)
# if element is not found it throws an exception.
a=nums.index(45,0) # 
print(a)
b=nums.index(45,a+1)
print(b)
c=nums.index(45,b+1)
print(c)
d=nums.index(45,c+1)
print(d)

# count() -->return frequency

a = nums.count(2)
print(a)

# sort --> descending to ascending order
# None return,
# inplace function
# no need of extra list(object)
nums.sort()# ascending order
print(nums)

nums.sort(reverse=True)# decreasing order
print(nums)

# inplace function are the function in which no extra object has been created  