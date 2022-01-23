import re
regexMail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
regexPass = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
regexMobile = re.compile(r'^01[0125][0-9]{8}$')
def isValidMobile(mobile):
    if re.fullmatch(regexMobile , mobile):
       return mobile
    else:
        mobile = isValidMobile(input("Plz, Enter your Egyption Mobile Phone"))
def isValidMail(email):
    if re.fullmatch(regexMail, email):
      return email
    else:
        email = isValidMail(input("Plz, Enter Valid Email: "))

def isValidPass(password):
    if re.fullmatch(regexPass , password):
       return password
    else:
        password = isValidPass(input("Plz, Ennter Valid Password Must Contain Lowercase , Uppercase  , Number and any Special Characters: "))

def isConfirmedPass(confirm_pass ,password):
    if confirm_pass != password:
        confirm_pass = isConfirmedPass(input("Enter your confirm pass") , password)
    else:
        return confirm_pass






greating= int(input("Hy! For Register press 1, For Log in press 2: "))

if greating == 1:
    first_name = input("Plz, Enter your First Name: ")
    last_name = input("Plz, Enter your Last Name: ")
    email = isValidMail(input("Plz, Enter Valid Email: "))
    password = isValidPass(input("Plz, Ennter Valid Password Must Contain Lowercase , Uppercase  , Number and any Special Characters: " ))
    confirm_pass = isConfirmedPass(   input("Plz, Confirm your password: " ) , password)
    mobile = isValidMobile(input("Plz, Enter your Egyption Mobile Phone: "))
    with open("users.txt", "a+") as users_file:
        #Move curser to the start file
        users_file.seek(0)
        # If file is not empty then append '\n'
        data = users_file.read(100)
        if len(data) > 0 :
            users_file.write("\n")
        users_file.write(first_name )
        users_file.write(" ")
        users_file.write(last_name)
        users_file.write(" ")
        users_file.write(email)
        users_file.write(" ")
        users_file.write(password)
        users_file.write(" ")
        users_file.write(confirm_pass)
        users_file.write(" ")
        users_file.write(mobile)
        users_file.write(" ")
    greating = int(input("Hy! For Register press 1, For Log in press 2: "))
#####################################################################################################################################
def checkLogIn(email):
    with open("users.txt" , "r") as logedUsers:
        if email in logedUsers.read():
            return email
        else:
            email = checkLogIn( input("Enter your Registed Mail: ") )

def correctPass(password):
    with open("users.txt" , "r") as logedUsers:
        if password in logedUsers.read():
            return password
        else:
            password = correctPass(input("Enter your password: "))




if greating == 2 :
    email = checkLogIn( input("Enter your Registed Mail: "))
    password = correctPass(input("Enter your password: "))
    project =int(input("Welcome, For creating new project press 1, For list all project press 2 , press 0 for exit:  "))
    if project == 1:
        title = input("Plz, Enter project title")
        details = input("Plz, Enter project details")
        totalTarget = int(input("Plz, Enter total target "))
        startDate = input("Plz, Enter start Date")
        endDate = input("Plz, Enter End Date")
        with open("projects.txt" , "a+") as projects:
            projects.seek(0)
            data = projects.read(100)
            if len(data) > 100:
                projects.write("\n")
            projects.write(title)
            projects.write(" ")
            projects.write(details)
            projects.write(" ")
            projects.write(str(totalTarget))
            projects.write(" ")
            projects.write(startDate)
            projects.write(" ")
            projects.write(endDate)
            projects.write(" ")

    elif project == 2:
        allProjects = open("projects.txt")
        projectsContent = allProjects.read()
        print(projectsContent)

    elif project == 0 :
        exit()
    else:
        print("Enter Vaild Number")

