list_t = [1,2,3,4,5,"a","ali",[1,2,3,4,5]]
print(list_t)
print(type(list_t))
print(list_t[0])
list_t[0] = "a"
print(list_t)

"""add element"""
list_t.append("b")
print(list_t)
print(len(list_t))

list_t.insert(1 , "c")
print(list_t)
print(len(list_t))

print(list_t[0:6:3])


"""tuple"""
tuple_t = tuple(list_t)
print(tuple_t)
print(type(tuple_t))

