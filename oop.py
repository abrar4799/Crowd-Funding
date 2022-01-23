
import re
class Users:
    def __init__(self , first_name , last_name ,email , password , confirm_password , mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.mobile = mobile
    def register(self  ):
            return f"{self.first_name}{self.last_name}{self.email}{self.password}{self.confirm_password}{self.mobile}"


class Projects:
    def __init__(self , title , details , totalTarget , startDate , endDate):
        self.title = title
        self.details = details
        self.totalTarget = totalTarget
        self.startDate = startDate
        self.endDate = endDate
    def creatingProject(self):
        return f"{self.title}{self.details}{self.totalTarget}{self.startDate}{self.endDate}"

def validMail(email):
    regexMail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regexMail , email):
        return email
    else:
      Main()

def validPassword(password):
   regexPass = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
   if re.fullmatch(regexPass , password):
       return password
   else:
       Main()

def confirmedPassword(confirm_password , password):
    if confirm_password != password:
        Main()
    else:
        return  confirm_password

def isValidMobile(mobile):
    regexMobile = re.compile(r'^01[0125][0-9]{8}$')
    if re.fullmatch(regexMobile , mobile):
        return mobile
    else:
        Main()
#################################################################
def savingUsers(fname , lname , email , password , confirm_password , mobile):
    with open("usersOOP.txt" , "a+") as usersOOP:
       usersOOP.write(fname)
       usersOOP.write(" ")
       usersOOP.write(lname)
       usersOOP.write(" ")
       usersOOP.write(email)
       usersOOP.write(" ")
       usersOOP.write(password)
       usersOOP.write(" ")
       usersOOP.write(confirm_password)
       usersOOP.write(" ")
       usersOOP.write(mobile)
       usersOOP.write(" ")

def savingProjects(title , details , totalTarget , startDate , endDate):
    with open("projectsOOP.txt" , "a+") as projectsOOP:
        projectsOOP.write(title)
        projectsOOP.write(" ")
        projectsOOP.write(details)
        projectsOOP.write(" ")
        projectsOOP.write(str(totalTarget))
        projectsOOP.write(" ")
        projectsOOP.write(startDate)
        projectsOOP.write(" ")
        projectsOOP.write(endDate)
        projectsOOP.write(" ")

def listProjects():
    allProjects = open("projectsOOP.txt")
    projectsContent = allProjects.read()
    print(projectsContent)


def checkEmail(email):
    with open("usersOOP.txt" , "r") as logedUsers:
        if email in logedUsers.read():
            return email
        else:
            print("You must Register First.")
            Main()

def checkPassword(password):
    with open("usersOOP.txt" , "r") as logedUser:
        if password in logedUser.read():
            return password
        else:
            print("Enter your correct password")
            Main()

def logIn(email , password ):
    return checkEmail(email) , checkPassword(password)



def Main ():
    greating = int(input("Hy! For Register press 1, For Log in press 2: "))
    if greating == 1:
     fname = input("Plz, Enter your first name: ")
     lname = input("Plz, Enter your last name: ")
     email = validMail(input("Plz, Enter your Email: "))
     password = validPassword(input("plz, Enter your password: "))
     confirm_password = confirmedPassword(input("Plz, Confirm your password: ") , password)
     mobile = isValidMobile(input("plz, Enter your phone: "))
     user = Users(fname, lname , email , password , confirm_password , mobile)
     savingUsers(fname , lname , email , password , confirm_password , mobile)
     user.register()

    elif greating == 2:
        email = input("plz, Enter your email: ")
        password = input("plz , Enter your password: ")
        logIn(email , password)
        projects = int(input("Welcome, For creating new project press 1, For list all project press 2 , press 0 for exit:  "))
        if projects == 1:
            title = input("Plz, Enter title of the project: ")
            details = input("Plz , Enter  details of the project ")
            totalTarget = int(input("Plz , Enter total taget of the project"))
            startDate = input("Plz , Enter start date ")
            endDate = input("Plz, Enter End Date")
            objectProject = Projects(title , details , totalTarget , startDate , endDate )
            savingProjects(title , details , totalTarget , startDate , endDate)
            objectProject.creatingProject()
        elif projects == 2:
            listProjects()
        elif projects == 0:
            exit()
        else:
            print("Enter Valid Option")

    else:
        print("Enter Valid Option")
        Main()

Main()






















