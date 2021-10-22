# this is the list from our last challenge 3-6:

guests = ['ali', 'tony', 'tia', 'sara', 'samer', 'ahmed', 'mouhammed', 'gabby']

message = "sorry guys as it seems I can invite only two for now"
print(message)


popped_guest = guests.pop()
print("Sorry " + popped_guest.title() + " I can't invite you")
popped_guest = guests.pop()
print("Sorry " + popped_guest.title() + " I can't invite you")
popped_guest = guests.pop()
print("Sorry " + popped_guest.title() + " I can't invite you")
popped_guest = guests.pop()
print("Sorry " + popped_guest.title() + " I can't invite you")
popped_guest = guests.pop()
print("Sorry " + popped_guest.title() + " I can't invite you")
popped_guest = guests.pop()
print("Sorry " + popped_guest.title() + " I can't invite you")

print(guests)

# informing the remaining guests

for guest in guests:
	print("Dear " + guest.title() + " you're still invited")
	
# delete the list

del guests[0:2]
print(guests)

