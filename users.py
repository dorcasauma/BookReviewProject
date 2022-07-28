from atexit import register
from multiprocessing import Condition
from typing import List
from datetime import datetime
import string
import csv

myfinalregister = []

# exception throw when username does not exist 
class InvalidUsername(Exception):
    pass 

# exception throw when password is invalid
class InvalidPassword(Exception):
    pass 

# exception throw when registering a user who already exist
class UserAlreadyExist(Exception):
    pass 


# exception thrown when registering a user with password missmatch i.e password 1 and 2 are not same 
class PasswordMissmatch(Exception):
    pass 


class InvalidDateOfBirth(Exception):
    pass

def read_file():
    mydata = []
    with open('bookreview_users.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row == []:
                pass
            else:
                mydata.append(row)
    return mydata
            
    
def mybookreview_users():
    userfound = False
    for i in myfinalregister:
        header = list(i.keys())
        data = list(i.values())
        k = read_file()
    if k == []:
        with open('bookreview_users.csv','a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            writer.writerow(data)
    else:
       for i in k:
           if data[0] in i :
               userfound = True
               raise UserAlreadyExist("The user already exits")
       if userfound == False:
           with open('bookreview_users.csv','a') as csv_file:
               writer = csv.writer(csv_file)
               writer.writerow(data)
            
            
            
def clear_users():
    """ only used when running tests"""
    pass

def login(username: str, password: str) -> dict:
    """ 
        Returns user details if user exist else returns None
    """
    myusers = read_file()
    the_user = {}
    users_password = ''
    count = 0
    for i in myusers:
        count+=1
        if username in i[0]:
            for k in i:
               l =  i.index(k)
               if l == 0:
                   the_user['username'] = k
               elif l == 1:
                   the_user['password'] = k
                   users_password = k
               else:
                   the_user['dateOfBirth'] = k
            
            if password == users_password:
                return the_user
            else:
                raise InvalidPassword("invalidpassword")
    if the_user == {} and count == len(myusers):
        raise InvalidUsername("invalid username")
def verifyDateofBirth2(dateOfBirth):
    correct_date_format = True
    try:
        datetime_object = datetime.strptime(dateOfBirth, '%d/%m/%Y')
            
        if datetime_object.year > datetime.today().year:
            correct_date_format = False
            
    except:
        correct_date_format = False
    return correct_date_format
    
    
def register(username: str, password: str, password2: str, dateOfBirth: str):
    """
    if user exist return error saying user already exist

    if password1 and password2 are equal and username does not exist it will create
    a new user on our user dictionary and return user.

    if password1 and password2 is not equal raise an error.
    """
    mycondition = False
    myregister = {}
    for i in myfinalregister:
        if username in i.values():
            mycondition = True
            raise UserAlreadyExist("The user already exits")
    else:
        k = verifyDateofBirth2(dateOfBirth)
        if k == True:
            if mycondition == False:
                if password == password2:
                    myregister['username'] = username
                    myregister["password"] = password
                    myregister["dateOfBirth"] = dateOfBirth
                    myfinalregister.append(myregister)
                    myfile = mybookreview_users()
                        
                else:
                    raise PasswordMissmatch("invalid password")
        else:
            raise InvalidDateOfBirth('InvalidDateOfBirth')
        
       
    return myregister

def list_users() -> List:
    pass 

if __name__ == '__main__':
    """ You can put your testing logic here """
    pass 

# from datetime import datetime
# datetime_object = datetime.strptime('12/12/2012', '%d/%m/%Y')