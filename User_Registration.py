#Registration and Login System using python

import re
#Setting constraints for Username and Password
user_reg = '^([A-Z|a-z])+\d*[^.]@[a-z]+.[a-z]+'
password_log = '^((?=.*[a-z]))((?=.*[A-Z]))(?=.*\d)((?=.*[!@#$%^&.+]))[A-Za-z\d!@#$%^&.+]{5,16}$'

# Opening a blank text file to store the username & password
Data = open("newfile.txt", "a")
Data.write("")
Data.close()

# Code to Register the username 
def register(Username=None,Password= None):
  Username = input("Enter a username:")
  Password = input("Create password:")

  if(re.search(user_reg,Username)):
    if(re.search(password_log,Password)):
      db1 = open("newfile.txt", "a")
      db1.write(Username+','+Password+"\n")
      print("User created successfully!")
      print("Registration Successful. Please proceed !")	
    else:
      print("Not Valid Password, Register again!")
      register()
  else:
    print('Enter a valid Username')
    register()

# Code to verify the username, if an existing user comes for registration 
def login(Username=None,Password= None):
  Username = input("Enter your username:")
  Password = input("Enter your password:")

  if(re.search(password_log,Password)):
    db1 = open("newfile.txt", "r")
    #db1.read()
    d = []
    f = []
    for i in db1:
      a,b = i.split(",")
      b = b.strip()
      d.append(a)
      f.append(b)
      data = dict(zip(d, f))

    try:
      if Username in data:
        try:
          if Password == data[Username]:
            print('Login Successful')
            print('Hi', Username)
          else:
            print('Wrong Password!')
        except:
          print('Incorrect passwords or username')
      else:
        print("Username doesn't exist")
        register()
    except:
      print("Password or username doesn't exist")
  else:
    print("Incorrect Password. Please attempt login again!")

# Code to change a password by verifing the username, if an existing user forgets the password.
def forgotpassword(Username=None, Password=None):
    Username = input("Enter your username:")

    if (re.search(user_reg, Username)):
        with open("newfile.txt", "r") as f:
            data = f.read()
        l = data.split('\n')
        #print(l)

        for i in range(0,len(l)-1):
            search = l[i]
            a, b = l[i].split(",")
            if a == Username:
              New_password = input("Enter your new password:")
              if(re.search(password_log,New_password)):
                new = Username + ',' + New_password
                replace = data.replace(search, new)
                with open("newfile.txt", "w") as f:
                    f.write(replace)
                print("Password updated successfully")
                break
              else:
                print("Enter a Valid Password")
                break
        else:
          print("User doesn't exists")
      
#Main fuction to decide the option an user wants to opt for.
def home(option=None):
  print("Welcome, please select an option")
  option = input("Login | Signup | Forgot Password:")
  if option == "Login":
    login()
  elif option == "Signup":
    register()
  elif option == "Forgot Password":
    forgotpassword()
  else:
    print("Please enter a valid parameter, this is case-sensitive")
 
home()
