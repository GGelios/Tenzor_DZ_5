
def password(passwd):
    if len(passwd)>=6:
         if [s for s in passwd if s in '1234567890']:
             if passwd.isdigit()==False:
                  if passwd.find=='password':
                      return False
                  else:
                      print('Your password fits the conditions')
                      return True 
             else:
                 print("Error. Your password doesn't fit")
                 return False
         else:
            print("Error. Your password doesn't fit")
            return False
    else:
        print("Error. Your password doesn't fit")
        return False
password(input('Enter the password: '))