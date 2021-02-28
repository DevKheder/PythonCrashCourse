#3-3 your_own_list favorite car models

favorite_old_car_models = ['cadillac coupe deVille 1977',
								'mercedes-benz 500-sel 1985',
								'buick lesabre 1994',
								'jaguar xj 1995'
								]


print(favorite_old_car_models[0].title())
print(favorite_old_car_models[1].title())
print(favorite_old_car_models[2].title())
print(favorite_old_car_models[3].title())


#or using a for loop

print("\nMy Favorite old-fashion car models are:")
for myFavorite_car in favorite_old_car_models:
	print("\n" + myFavorite_car)
