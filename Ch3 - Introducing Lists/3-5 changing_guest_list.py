#3-5 Changing guest list

suggested_names = ['mary', 'souzan', 'samy']

print("\nOne of them can't make it: \n")

popped_name = suggested_names.pop()
print(popped_name.title() + " can't make it, I guess I have to think of another name now.")

print("\nNow Modifying the list\n")

new_name = "eddie"

suggested_names.append(new_name)

print(suggested_names)

for name in suggested_names:
	print("\n" + 
		name.title() + 
		", I would like to invite you to the dinner.")
