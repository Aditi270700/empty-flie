# slicing use of list and tuple

#taking some part of lis is called slicing
#      0 1 2     3       4  5 6    7     8  9 10
lis1=[12,3,44,'saurabh',56,7,88,'aditya',33,4,5]
#   -11 -10 -9  -8      -7-6-5    -4     -3-2-1

print(lis1)
# lis[start:end:jump]
# jump--->default 1
# end --->excluded(just before end)

a=lis1[3:8:1]
print(a)
b=lis1[3:8:1]
print(b)

#slicing is used to get slice (subsequence) of a sequence datatype