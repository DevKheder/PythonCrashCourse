# creating a list of guests

guests = ["modar", "sara", "samer", "ahmed", "mouhammed"]

# storing the name of the guest who can't make it to dinner
popped_guest = guests.pop(0)

# print a message and inform the name who can't make it
print("I am afraid " + popped_guest.title() + " can't make it to the dinner")

# replacing the popped guest with another person
new_guest = guests.insert(0, 'tony')
print(guests)

# using the for loops to print a message for each person

for guest in guests:
	print("Howdyy, " + guest.title() + " I would like to invite you for a dinner")
