# # print('SIGN UP')
# # username=input('Enter Your FullName')
# # userpass=input('Enter Your Password')
# # if len(userpass)>=8:
# #     print("sucessfully signed up")
# #     print('login section is open')
# #     userL=input('enter your name')
# #     passL=input('enter password')
# #     if (userL==username) & (passL==userpass):
# #         print('login successfully')
# #     else:
# #         print('Your details not match,try again')
# # else:
# #  print('password requirement doesn\'t meet , please try again...') 




# print('SIGN UP')
# username=input('Enter Your FullName ')
# userpass=input('Enter Your Password ')
# while len(userpass)<8 or userpass.isalnum():
#    print('password formate not match ')
#    username=input('Enter Your FullName ')
#    userpass=input('Enter Your Password ')
# else:
#    if len(userpass)>=8:
#     print("sucessfully signed up")
#     print('login section is open')
#     userL=input('enter your name ')
#     passL=input('enter password ')
#     while (userL!=username) or (passL!=userpass):
#         print('password requirement doesn\'t meet , please try again...') 
#         userL=input('enter your name')
#         passL=input('enter password')
#     else:
#         print('login successfully')