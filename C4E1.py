#CIS41A C4E1 Jackie Wang junkaiwang0716@gmail.com a program that find the domain name of the email address
user_input = input("Enter an email address: ")

if "@" in user_input and "." in user_input:#check if it's a vaild email
    domain = user_input.split("@")[1].split(".")[0]#split mail domain from user input
    print(domain)
else:
    print("Invalid email address.")
'''
Enter an email address: junkaiwang0716@gmail.com
gmail

Enter an email address: junkaiwang0716gmail.com
Invalid email address.
'''