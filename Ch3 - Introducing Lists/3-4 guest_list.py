#3-4 Guest List

suggested_names = ['mary', 'souzan', 'samy']

print(suggested_names)

#now printing a message to invite each person

print("Hi " +
	suggested_names[0].title() + 
	", I would like to invite you to the dinner."
	)
	
print("Hi " +
	suggested_names[1].title() + 
	", I would like to invite you to the dinner."
	)	

print("Hi " +
	suggested_names[2].title() + 
	", I would like to invite you to the dinner."
	)

#or I could use a for loop
print("\nMy invitations: \n")
for person in suggested_names:
	print(person.title() + ", I would like to invite you to the dinner.")
