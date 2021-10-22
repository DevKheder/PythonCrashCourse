# creating a list of guests

guests = ["modar", "sara", "samer", "ahmed", "mouhammed"]

# storing the name of the guest who can't make it to dinner
popped_guest = guests.pop(0)

# print a message and inform the name who can't make it
print("I am afraid " + popped_guest.title() + " can't make it to the dinner")

# replacing the popped guest with another person
new_guest = guests.insert(0, 'tony')
print(len(guests))

# infroming the people that I just found a bigger table

message = "oh dears, i'm glad to tell you that now I found a bigger table"
message += " means more people are going to be invited"
print(message)


# adding more people using insert()

guests.insert(0, 'ali') 
guests.insert(2, 'tia')
guests.append('gabby')

for guest in guests:
	print(guest.title() + " you're invited to our dinner time")
