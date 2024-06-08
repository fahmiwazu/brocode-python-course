############# List
food = ["rendang","kebab","nasgor","borgar","podeng"]
print(food)
food[0]="Sambal"
food.append("Ice Cream")
food.remove("borgar")
food.pop()
food.insert(0,"cake")
food.sort()
food.clear()

for i in food:
    print(i)