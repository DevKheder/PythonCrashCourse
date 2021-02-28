#3-6 More Guests

suggested_names = ['mary', 'souzan', 'sam', 'eddie']

print("\nHey guys; it seems i'm going to expand my list because now I found a bigger table\n")


#adding a new name to the middle of the list
suggested_names.insert(2, 'sam')
print("Hi " + 
		suggested_names[2].title() + 
		", It would be my pleasure if you come and join us\n")

print(suggested_names)

#now adding a new name to the beginning of the list

suggested_names.insert(0, 'maria')
print("\n\nHi " + 
		suggested_names[0].title() + 
		", It would be my pleasure if you come and join us\n")
		
print(suggested_names)

#appending a new element or name

suggested_names.append('rachel')

print(suggested_names)

#I will use a for loop instead of writing many print statement

for person in suggested_names:
	print("\n\nHi " + 
			person.title() + 
			", It would be my pleasure if you come and join us\n")



