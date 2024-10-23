data = {'1':2390,'2':2387,'3':4533,'4':{'11':3523,'22':63634,'44':4574}}
print(type(data['4']))
print(type(data['1']))
print(type(data))
data['4'].popitem()
print(data)
data.popitem()
print(data)