#every function
#creating an empty list

languages = []

#adding items to the list

languages.append('english')
languages.append('russian')
languages.append('german')
languages.append('turkish')
print(languages)
print(languages[0].title())
languages.insert(3, 'arabic')
print(languages)

languages.sort(reverse=True)
print(languages)

languages.sort()
print(languages)

del languages[0]
print(languages)
languages.remove('german')
print(languages)

languages[2] = 'spanish'
print(languages)
print("End of the program")
#there are much more methods that we could have done in this example
#as we learned in the chapter 3

