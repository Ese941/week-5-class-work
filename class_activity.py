print("Welcome to the list generating app. We are here to help you generate a list of your favorite foods.")
food1=input("What is your first favorite food: \n")
food2=input("What is your second favorite food: \n")
food3=input("What is your third favorite food:  \n")
favorite_food=[food1, food2, food3]
print("Here are some operations you can carry out with your list : \n 1. Append \n 2. Clear \n 3. Copy \n 4. Count \n 5. Extend \n 6. Index \n 7. Insert \n 8. Pop \n 9. Remove \n 10. Reverse \n 11. Sort \n")
user=input("Pick one:")
if user == "1":
    add=input("What would you like to add to the list? ")
    favorite_food.append(add)
    print(favorite_food)


elif user == "2":
    favorite_food.clear()
    print(favorite_food)


elif user == "3":
    urlist=input("What do you want to copy: ")
    favorite_food=list(urlist)
    print(favorite_food)

elif user == "4":
    xs=input("What would you like to count: ")
    x=favorite_food.count(xs)
    print(x)
    
    
elif user == "5": 
    another1=input("Add one more food to your new list: \n")
    another2=input("Add one more food again to your new list:  \n")
    another3=input("Add the last food to your new list: \n")
    newlist=[another1,another2,another3]
    favorite_food.extend(newlist)
    print(favorite_food)
    
    
elif user == "6": 
    z=input("What food would you like to find the position of: ")
    zs=favorite_food.index(z)
    print(zs)


elif user == "7":
    c=int(input("what position would you like it to be at: \n"))
    cs=input("What food would you like to add: ")
    favorite_food.insert(c, cs)
    print(favorite_food)

elif user == "8": 
    g=int(input("What position would you like to change it to:"))
    gs=input("What food position would you like to change: ")
    favorite_food.pop(g,gs)
    print(favorite_food)


elif user == "9": 
    k=input("What food would you like to remove: ")
    favorite_food.remove(k)
    print(favorite_food)


elif user == "10": 
    h=list(reversed(favorite_food))
    print(h)


elif user == "11": 
    favorite_food.sort()
    print(favorite_food)
        
else:
    print("Oops that's not known, read the instructions and try again")


    





