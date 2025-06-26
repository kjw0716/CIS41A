#CIS41A C6E1 Jackie Wang  Friends list management that can find which year to associate with this friend also could add friends to lists
# Create 2017 and 2018 friends list
friends_2017 = ["Joe", "Lily"]
friends_2018 = ["Bob", "Tom"]

#Displays all freinds list
All_friends = friends_2017 + friends_2018
print("Friends List", All_friends)

#Get friend's name user try to search
name = input("Enter your friend's name:")

#Check firends is form which list
if name in friends_2017:
    print(name,"was found in 2017 list")
elif name in friends_2018:
    print(name,"was found in 2018 list")
else:
    print(name,"is not in any list")

#Add new firend to list
new_friend = input("Enter a new friend name: ")
year = input("Enter the year to associate with this friend : ")

#Check if user enter right year
if year == "2017":
    friends_2017.append(new_friend)
    print(new_friend, "has been added to the 2017 list.")
elif year == "2018":
    friends_2018.append(new_friend)
    print(new_friend, "has been added to the 2018 list.")
else:
    print("Invalid year")

#Display the updated 2017 and 2018 friends lists
print("friends_2017:", friends_2017)
print("friends_2018:", friends_2018)

'''
Friends List ['Joe', 'Lily', 'Bob', 'Tom']
Enter your friend's name:Joe
Joe was found in 2017 list
Enter a new friend name: Jackie
Enter the year to associate with this friend : 2018
Jackie has been added to the 2018 list.
friends_2017: ['Joe', 'Lily']
friends_2018: ['Bob', 'Tom', 'Jackie']

Friends List ['Joe', 'Lily', 'Bob', 'Tom']
Enter your friend's name:Jane
Jane is not in any list
Enter a new friend name: Jane
Enter the year to associate with this friend : 2017
Jane has been added to the 2017 list.
friends_2017: ['Joe', 'Lily', 'Jane']
friends_2018: ['Bob', 'Tom']
'''