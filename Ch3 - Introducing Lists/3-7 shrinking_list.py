#3-6 More Guests

suggested_names = ['mary', 'souzan', 'sam', 'eddie']


#shrinking guest list

print("Howdy friends!" +
		"I have just received a message from the resturant" +
		" telling me that there's only one table and for two person."
		"Sorry!!!"
		)
		
popped_name = suggested_names.pop()
print(popped_name)
popped_name_1 = suggested_names.pop()
print(popped_name_1)
	
print("sorry " + popped_name.title() + ", because I can't make it for you")
print("sorry " + popped_name_1.title() + ", because I can't make it for you") 
print(suggested_names)
	
#now lets remove the last remaining guests so the list becomes empty.
del suggested_names[0]

del suggested_names[0]
print(suggested_names)
