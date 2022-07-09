from email import message


first_name = 'george'
last_name = 'medler'
full_name = f'{first_name} {last_name}'
print(full_name)

message = f'Hello, {full_name.title()}!'
print(message)

message = f'{full_name.upper()}'
print(message)

library_name = ' salt lake county library '
message = f'{library_name.lstrip()}'
print(message)

message = f'{library_name.rstrip()}'
print(message)

library_name = library_name.strip()
message = f'{library_name.title()}'
print(message)


