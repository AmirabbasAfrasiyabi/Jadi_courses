"""set"""

list_t = [1,2,3,4,4,4,5,6,7,2,3]
set_t = set(list_t)
print(list_t)
print(type(list_t))
print(len(list_t))

print(set_t)
print(type(set_t))
print(len(set_t))

#add
set_t.add(5)
set_t.add(8)
print(set_t)
print(type(set_t))
(print(len(set_t)))


#logical property

set_1 = {1,2,3,4,5,6,7,8}
set_2 = {4,5,6,7,8,9,0,1}

print(set_1)
print(set_2)

print(set_1|set_2) #or
print(set_1&set_2)  #and
print(set_1 - set_2)  # (all -(and))

"""dictionary"""
dict_1 = {'amir' : '09120910309'
    ,'ati' : '09120034660'
    ,'reyhane' : '09126993119'
    ,'mother' : '09120781057'
    ,'father' : '09128433591'}

dict_1['amir'] = '09399814907'
print(dict_1['amir'])

print(dict_1.get('amir'))


for k,v in dict_1.items():
    print(k,v)