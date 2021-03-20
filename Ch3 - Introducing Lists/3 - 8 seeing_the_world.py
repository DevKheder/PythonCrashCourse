#3 - 8 seeing the world

#storing places in a list

places_to_visit = ['south island, new zealand', 
                   'new york city', 
                   'rio de janeiro',
                   'niagara falls',
                   ]

print("1-printing the list as it doesn't to be so neatly now!: \n")

print(places_to_visit)		
					
print("\n2-using the sorted method: \n")

print(sorted(places_to_visit))

#in the very recent code, we printed the 
#list in an alphabetical sorted order yet temporarly
print("\n3-the original order when we print the list again:\n")

print(places_to_visit)

print("\n4-printing the list in a reverse order using sorted method:\n")

#reversing the list
places_to_visit.reverse()
print(places_to_visit)
print(sorted(places_to_visit))

#showing the list in an original order
#note: reverse method doesn't apply any alphapetical re-positioning
print("\n5-print in the original order:\n")
places_to_visit.reverse()
print(places_to_visit)

#reversing the list
print("\n6-reversing the list:\n")
places_to_visit.reverse()
print(places_to_visit)

#reversing the list to show the original order
print("\n7-reversing the list to print the original order:\n")
places_to_visit.reverse()
print(places_to_visit)

#using the sort method
print("\n8-using the sort method:\n")
places_to_visit.sort()
print(places_to_visit)

#sort the list in a reverse order
print("\n9-printing the list using sort and reverse method:\n")
places_to_visit.sort(reverse=True)
print(places_to_visit)

#using the sort method so it's stored in a reverse order
print("\n10-printing the list using sort to store it reversed:\n")
places_to_visit.sort()
print(places_to_visit)
