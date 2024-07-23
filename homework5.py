#immutable_var = c
#print(immutable_var)
#immutable_var[0] = 3
#кортеж – это неизменяемая упорядоченная коллекция, которая может содержать в себе разные типы данных. 
mutable_list = ['peach', 'apple', 'cherry'] 
mutable_list[1] = 'banana'
print(mutable_list)
mutable_list.append(2)
print(mutable_list)
mutable_list.extend('HELLO')
print(mutable_list)