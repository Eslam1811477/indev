from pathlib import Path

def wpet():
    print('Welcome To "Export Theme" Method 😊😊😊\n')
    hmn2 = True
    while hmn2:
        theme_path = input('Please Inter Theme Path : ')
        if(len(theme_path) != 0):
            if Path(theme_path).is_dir():
                if Path.isfile(Path.join(theme_path, 'index.php')) & Path.isfile(Path.join(theme_path, 'function.php')) & Path.isfile(Path.join(theme_path, 'style.css')):
                    print('true')
                else:
                    print('This theme is incomplete and not suitable for extraction 🙂🙂🙂.')
                hmn2 = False
            else:
                print(f"The path '{theme_path}' is not a valid directory.")
            
        else:
            print('Unexpected Inputs !!')

