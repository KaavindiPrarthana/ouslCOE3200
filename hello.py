# Ask the user for their age
age = int(input("Please enter your age: "))

# Check if the user is under 18
if age < 18:
    print("You are under 18. You can join using this link: https://example.com/join")
else:
    print("You are 18 or older. Sorry, you cannot join.")
