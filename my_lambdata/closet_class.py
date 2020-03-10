from my_lambdata.my_class import My_Class

print('\n')

obj = My_Class('sweaters', 'red', 2)

print('*Checks closet*')
obj.check_closet()

print('\nLets go shopping for a different color jacket.')
obj.go_shopping()
print('You like the ' + obj.color + ' ' + obj.jacket_type + '.')

print('\nHow many of this new jacket do you want?')
obj.how_many()
print('You bought ' + str(obj.in_closet) + ' ' + obj.color + ' ' + obj.jacket_type)

print('\n')
