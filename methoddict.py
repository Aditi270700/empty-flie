# method of dict
# zip
names = ["Ajay","Vikas","Arun","Sonam","naman"]
value = [23,23,24,45,56]
result = dict(zip(names,value))
print(result)

result = tuple(zip(names,value))
print(result)

result = list(zip(names,value))
print(result)


# get function (get is dictionary function) it is return value

data = {'Ajay':23,'Vikas':23,'Arun':45}
a=data['Arun']
print(a)

b=data.get('Ashish')
print(b)


# setdefault()  under setdefault we pass the value
# 1) key available --> return existing value
# 2) key not available --> key-value pair add, return added value 
data = {'1':2390, '2':2387, '3':4533}
data.setdefault('1')
print(data)
value = data.setdefault('11',9999)
value = data.pop('2')
value = data.popitem() # delete last value key pair
print(data)
print(value)



# pop(), popitem(), clear()
