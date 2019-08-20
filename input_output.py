import math

# f-strings (formatted string literal)
# print(f'The vale of PI is approximately {math.pi:.3f}.')

# table = { 'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678 }
# for name, phone in table.items():
#     print(f'{name:10} => {phone:10d}')

spam_eggs = '{0} and {1}'.format('spam', 'eggs')
eggs_spam = '{1} and {0}'.format('spam', 'eggs')
print(spam_eggs)
print(eggs_spam)

by_reference = 'ref1 = {ref1}, ref2 = {ref2}'.format(
    ref1='text 1', ref2='text 2'
)
print(by_reference)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
by_dict = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d};\
           Dcab: {0[Dcab]:d}'.format(table)
derref = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)
print(by_dict)
print(derref)
