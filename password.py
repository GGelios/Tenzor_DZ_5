"""Написать функцию, принимающую строку-пароль. Функция должна проверить подходит ли этот пароль условиям и вернуть True - если подходит; False - если не подходит. Условия:   
        1. Должен быть не менее 6 символов;
        2. Должен содержать хотя бы одну цифру;
        3. Не должен состоять только из цифр;
        4. Не должен содержать слово “password” в любом регистре."""

def password(passwd):
    """Function password

    Accepts arguments - str and int and checks for conditions
    Returns the conditions for passing checks

    """
    if len(passwd) >= 6 and [s for s in passwd if s in '1234567890'] and passwd.isdigit() == False:
        if passwd.find == 'password':
            return False               
        else:
            print('Your password fits the conditions')
            return True                
    else:
        print("Error. Your password doesn't fit")
        return False                 

password(input('Enter the password: '))
