print("Monkey Business Employee Info")
username = None
password = None
flub_username = "monkey"
flub_password = "monkey"
flub_todo1 = "eat bananas,"
flub_todo2 = "eat bananas,"
flub_todo3 = "eat bananas"
flub_role = "Role: CEO"
username = input("What is your Monkey Business username? ")
password = input("What is your Monkey Business password? ")
if username == flub_username and password == flub_password:
    print("Welcome Flub!")
    print(flub_role)
    print("To Do's:", flub_todo1, flub_todo2, flub_todo3)
