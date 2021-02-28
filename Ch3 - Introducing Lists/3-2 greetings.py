#3 - 2 Greetings


friends_names = ['iguana', 'chris', 'tawfeek', 'tindra']


print(friends_names[0].title() + ", you're very welcome")
print(friends_names[1].title() + ", you're very welcome")
print(friends_names[2].title() + ", you're very welcome")
print(friends_names[3].title() + ", you're very welcome\n")

#I added a new line in the last print statement in order to speerate the block from the next one
#or we'd make it shorter by using the for loop

for friend in friends_names:
	print("\n" + friend.title() + ", you're very welcome!")
