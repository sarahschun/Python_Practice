friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_numbers = [4, 8, 15, 16, 23, 42]
# print all
#  \print(friends)

# print certain ones
# print(friends[0])
# print(friends[-1])
# print(friends[1:3])

# add two lists together
friends.extend(lucky_numbers)

# add item to list
friends.append("Sarah")

# special add item
friends.insert(1, "Kelly")

# remove item
friends.remove("Jim")

# removes last item
friends.pop()

# find certain element in list
friends.index("Kevin")

# count number of items with same value
friends.count("Jim")

# sort list in ascending/ alpha
friends.sort()

# reverse list
lucky_numbers.reverse()

# copy list
friends2 = friends.copy()
