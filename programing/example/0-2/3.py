list_1 = [1,2,3,4,5]
list_2 = [4,5,6,7,8]

final_list = list_1 + list_2
print(final_list)


final_list = list(set(list_1 + list_2))
print(final_list)

print(final_list[:3])