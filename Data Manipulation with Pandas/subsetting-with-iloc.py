# Make a list of cities to subset on
cities = ['Moscow','Saint Petersburg']
#print(cities)
# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])
