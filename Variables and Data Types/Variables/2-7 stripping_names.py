#2-6 Stripping Names

#playing around with stripping, lowercase, uppercase and extra new_lines and tabs 

name = "  magnus   "
print(name.lstrip().lower())
print(name.rstrip())

name = name.strip()
print(name)
print("\t\t\t\t\t" + name)
print("\n\n\n\t\t\t" + name.upper())

#adding tabs and new lines
name_2 = "k\n\th\n\t\te\n\t\t\td\n\t\t\t\te\n\t\t\t\t\tr"
print(name_2)


#stripping methods can't get the whitespace made with \t and \n removed
name_2 = name_2.strip()
print(name_2)
name_2 = name_2.lstrip()
print(name_2)
name_2 = name_2.rstrip()
print(name_2)
