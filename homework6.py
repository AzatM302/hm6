my_dict = {'Phone 1': 9377712345, 'Phone 2': 9393081234, 'Phone 3': 917917321}
print(my_dict)
print(my_dict.get('Phone 1'))
print(my_dict.get('Phone'))
my_dict.update({'Phone 5': 12345678, 'Phone 6': 987654321})
print(my_dict)
a = my_dict.pop('Phone 1')
print(a)
print(my_dict)
my_set = {1,1,2,2,3,3,'a','b','b'}
print(my_set)
my_set.update({True, '123'})
print(my_set)
my_set.discard(3)
print(my_set)