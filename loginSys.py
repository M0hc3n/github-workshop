class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def check_password(self, password):
        return self.password == password

    def print(self):
        print("Username : ", self.name)
        print("Password : ", self.password)
    

users =[]

def print_table():

    while True :
        print(".Welcome to the main board, enter your choice : ")
        print("        1- Sign up for a new account.")
        print("        2- Sign in to your account.")
        print("        3- Print All.")
        print("        4- Exit")
        choice = int(input())

        if choice == 1:
            Sign_up()
        elif choice ==2:
            Sign_in()
        elif choice ==3:
            print_All()
        elif choice==4:
            break
        else:
            print("---> Please enter a valid choice.")

def check_if_exists(users, name, password):
    for user in users:
        if( user.name == name and user.password == password):
            return True
    
    return False

def add_user(users, name, password):
    users.append(User(name, password))

def Sign_up():
    print("Sign Up:")
    print("Enter Username : ")
    name = input()
    print("Enter password : ")
    password = input()

    if(check_if_exists(users, name, password)):
        print("Already existing credientials...  Enter other ones.")
        Sign_up()
    else :
        add_user(users, name, password)
        print("User added successfully.")
    

def Sign_in():
    print("Sign In:")
    print("Enter Username : ")
    name = input()
    print("Enter password : ")
    password = input()

    if(check_if_exists(users, name, password)):
        print("You are logged in your Account.")
    else:
        print("Wrong credientials... Please make sur to sign up first.")

def print_All():
    for user in users:
        user.print()
        print("---------------------")

print_table()


    
