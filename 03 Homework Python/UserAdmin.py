# Administrator accounts list
adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]



# Build your login functions below
def getCreds():
    # Prompt the user for their username
    username = input("What's your username? ")
    # Prompt the user for their password
    password = input("What's your password? ")

    # Create a dictionary, called `userInfo` with the keys "Username" and "Password"
    # Associate these keys with the values the user entered
    userInfo = {
        "username": username,
        "password": password
    }

    
   # Return user
   # return user_info

    return userInfo
    

#getCreds(user_info)
#  Check the information that was entered against the admin list
#  If the information is in the list it returns True, otherwise False

def checkLogin(userInfo, adminList):
    # loggedIn = True
    if userInfo in adminList:
        #  print("Already Used")
        return True        
    else:
        return False
                



#  userInfo = getCreds()
#  loggedIn = checkLogin(userInfo, adminList)

#While loop:  Continues to run each function getCreds() and checkLogin(userInfo, adminList) untill the correct information it entered   
loggedIn = False
while loggedIn == False:
    userInfo = getCreds()
    loggedIn = checkLogin(userInfo, adminList)
    print("-----------------------")
    #retry = input("go again? (y)es or (n)o ")

print("YOU HAVE LOGGED IN!")
    


   