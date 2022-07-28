import sys
from turtle import pd 
from users import register, login,verifyDateofBirth2
command_line_inputs = sys.argv
print(command_line_inputs)
credentials = []
for i in command_line_inputs:
    if "=" in i:
       k =  i.split("=")
       credentials.append(k[1])
if command_line_inputs[1] == 'user_register':
    username = credentials[0]
    password = credentials[1]
    password2 = credentials[2]
    dateOfBirth = credentials[3]
    print(register(username,password,password2,dateOfBirth))
else:
    username = credentials[0]
    password = credentials[1]
    print(login(username,password))
       
       
