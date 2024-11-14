candies = [2, 3, 5, 3, 1, 3]
exctraCandies = 2
max_candies = max(candies)
return_list = []
for candy in candies:
    return_list.append(candy + exctraCandies >= max_candies)
print(return_list)