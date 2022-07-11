dinner_guests = ['callie', 'corrine', 'cambrea']
invite_message = 'I would love to invite you to join me for dinner tomorrow evening at 6 pm.'

print(f'{dinner_guests[0].title()}, ' + invite_message + '\n')

print(f'{dinner_guests[1].title()}, ' + invite_message +'\n')

print(f'{dinner_guests[2].title()}, ' + invite_message + '\n')

cannot_come = 'corrine'
dinner_guests[1] = 'andrea'
print(cannot_come + '\n\n')

print(dinner_guests)

print(f'{dinner_guests[0].title()}, ' + invite_message + '\n')
print(f'{dinner_guests[1].title()}, ' + invite_message + '\n')
print(f'{dinner_guests[2].title()}, ' + invite_message + '\n')

print('I found a bigger table so I will be inviting more people. Yay!\n\n')

dinner_guests.insert(0,'daphne')
print(dinner_guests)

dinner_guests.insert(2, 'kelli')
print('\n')
print(dinner_guests)

dinner_guests.append('amanda')
print('\n')
print(dinner_guests)
print('\n')

print(f'{dinner_guests[0].title()}, ' + invite_message + '\n')
print(f'{dinner_guests[1].title()}, ' + invite_message + '\n')
print(f'{dinner_guests[2].title()}, ' + invite_message + '\n')
print(f'{dinner_guests[3].title()}, ' + invite_message + '\n')
print(f'{dinner_guests[4].title()}, ' + invite_message + '\n')
print(f'{dinner_guests[5].title()}, ' + invite_message + '\n')

print('Oh, no! My new table won\'t fit, so I can only invite two people!\n')

uninvite_guest_1 = dinner_guests.pop(0)
uninvite_message = 'I\'m so sorry, I can only have two people come to dinner tomorrow so I\'ll have to have you come another time.'

print(f'{uninvite_guest_1.title()}, ' + uninvite_message + '\n')

print(dinner_guests)





