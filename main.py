import bcrypt
import re

regex = re.compile(r"(^[a-zA-Z]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)")
r_p = re.compile(r"(^(?=\S{5,16}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')")

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email.")
    else:
      print("Invalid email. Please Try Again")
      register()

def isValid1(password1):
    if re.fullmatch(r_p, password1):
      print("Valid password.")
    else:
      print("Invalid password. Please Try again \n The password should contain: \n min length is 5 and max length is 16 \n at least include a digit number \n at least a upcase and a lowcase letter \n at least a special characters")
      register()


def welcome():
    print("Welcome to your dashboard")


def gainAccess(Username=None, Password=None):
    Username = input("Enter your username:")
    Password = input("Enter your Password:")

    if not len(Username or Password) < 1:
        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                c = a, b
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if Username in data:
                    hashed = data[Username].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')

                    try:
                        if bcrypt.checkpw(Password.encode(), hashed):

                            print("Login success!")
                            print("Hi", Username)
                            welcome()
                        else:
                            print("Wrong password. Please try login again")
                            home()

                    except:
                        print("Incorrect passwords or username. Please try to login again")
                        home()
                else:
                    print("Username doesn't exist. Please try to login again")
                    home()

            except:
                print("Password or username doesn't exist. Please proceed with Signup")
                home()
        else:
            print("Error logging into the system.Please try to login again")
            home()

    else:
        print("Please attempt login again")
        gainAccess()

    # b = b.strip()


# accessDb()

def register(Username=None, Password1=None, Password2=None):
    Username = input("Enter a username:")
    isValid(Username)
    Password1 = input("Create password:")
    isValid1(Password1)
    Password2 = input("Confirm Password:")
    db = open("database.txt", "r")
    d = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        c = a, b
        d.append(a)
    if not len(Password1) <= 8:
        db = open("database.txt", "r")
        if not Username == None:
            if len(Username) < 1:
                print("Please provide a username")
                register()
            elif Username in d:
                print("Username exists")
                register()
            else:
                if Password1 == Password2:
                    Password1 = Password1.encode('utf-8')
                    Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())

                    db = open("database.txt", "a")
                    db.write(Username + ", " + str(Password1) + "\n")
                    print("User created successfully!")
                    print("Please login to proceed:")
                    home()


                # print(texts)
                else:
                    print("Passwords do not match")
                    register()
    else:
        print("Password too short")


def home(option=None):
    print("Welcome, please select an option")
    option = input("Login | Signup:")
    if option == "Login":
        gainAccess()
    elif option == "Signup":
        register()
    else:
        print("Please enter a valid parameter, this is case-sensitive")
        home()


# register(Username, Password1, Password2)
# gainAccess(Username, Password1)
home()
