def print_large_blue_text():
    # ANSI escape codes for color and style
    blue_color = "\033[34m"  # Blue color code
    reset = "\033[0m"  # Reset to default color
    large_font = '''
    PPPPP   AAAAA  SSSSS  SSSSS  W   W  OOO  RRRRR   DDDD  
    P   P  A     A S      S      W   W O   O R    R  D   D 
    PPPPP  AAAAAAA SSSSS  SSSSS  W W W O   O RRRRR   D   D 
    P      A     A     S      S  W W W O   O R   R   D   D 
    P      A     A SSSSS  SSSSS  W W W OOO  R    R  DDDD  
    '''

    print(blue_color + large_font + reset)
print_large_blue_text()

list=["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H",  "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" ,"V" , "W" ,"X" ,"Y" , "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y" , "z" ,"!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]","|",":",";","<",">",".","?","/"]
from random import *
letters=(list[randint(1,26)])
other_letters=(list[randint(1,52)])
another_letters=(list[randint(27,52)])
another_numbers=str((randint(0,9)))
symbol=(list[randint(53,77)])
another_symbol=(list[randint(53,77)])

print("\033[32mThe owner is : HAIBARA CONAN\033[0m")

recommended=input("Do you want recommended length for password (y/n) :")
if recommended.upper() == 'YES' or recommended.upper() == 'Y' :
    password=str(numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol
    print( f'Your generated password is : {str(numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol}')
else:
    number = input("Choose the length of the password (3 < length <= 13) : ")
    if number == 0 :
        print("Invalid")
    elif number ==1 or number ==2 or number ==3 :
        print("Put some effort !!!")
    elif number == "4" :
        password= str(another_letters) + symbol +  another_numbers + letters
        print(f'Your generated password is : {  str(another_letters) + symbol +  another_numbers + letters }')
    elif number == "5":
        password=letters + str(another_numbers) + symbol  + other_letters  + another_letters
        print(f'Your generated password is : {  letters + str(another_numbers) + symbol  + other_letters  + another_letters }')
    elif number == "6":
        password=str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters
        print(f'Your generated password is : {str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters }')
    elif number == "7" :
        password=str(another_numbers) + letters + other_letters + symbol + another_letters + other_letters + another_symbol
        print(f'Your generated password is : {str(another_numbers) + letters + other_letters + symbol + another_letters + other_letters + another_symbol}')
    elif number == "8" :
        password=str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol
        print(f'Your generated password is : {str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol}')
    elif number == "9" :
        password=str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol + other_letters
        print(f'Your generated password is : {str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol + other_letters }')
    elif number == "10" :
        password=str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol + letters +letters
        print(f'Your generated password is : {str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol + letters +letters }')
    elif number == "11" :
        password=str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol + other_letters + another_letters
        print(f'Your generated password is : {str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol + other_letters + another_letters}')
    elif number == "12" :
        password=str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol + other_letters + another_letters + another_symbol
        print(f'Your generated password is : {str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol + other_letters + another_letters + another_symbol}')
    elif number == "13":
        password=str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol + other_letters + another_letters + another_symbol +letters
        print( f'Your generated password is : {str(another_numbers) + letters + other_letters + symbol + str(another_numbers) + another_letters + other_letters + another_symbol + other_letters + another_letters + another_symbol +letters}')
    else :
        print("Invalid")
