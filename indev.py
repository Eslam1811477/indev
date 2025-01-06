import pyfiglet

fig = pyfiglet.Figlet(font='slant')
print(fig.renderText("Indev"))


print('Methods:')
print('1. Export WordPress Theme')
print('\n')



def wpet():
    print('Welcome To "Export Theme" Method 😊😊😊\n')
    hmn2 = True
    while hmn2:
        theme_path = input('Please Inter Theme Path : ')
        if(len(theme_path) != 0):
            print('smm')
            hmn2 = False
        else:
            print('Unexpected Inputs !!')















hmn = True
while hmn:
    method_number = input('Enter Your Method Number: ')
    try:
        method_number = int(method_number)
        if method_number == 1:
            print('Method 1 selected')
            wpet()
        elif method_number == 2:
            print('Method 2 selected')
        elif method_number == 3:
            print('Method 3 selected')
        else:
            print('Invalid method number')
        hmn = False
    except ValueError:
        print('Not an integer. Exiting...')
