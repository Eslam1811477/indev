import zipfile
import os
import json

def zip_directory_with_exclusions(directory, exclusions):
    output_zip = input('Enter Theme Name: ')
    if(output_zip == ''):
        output_zip = 'theme'
    if('.' not in output_zip):
        output_zip = output_zip + '.zip'
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in exclusions]
            for file in files:
                print('File: '+file)
                if file not in exclusions:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=os.path.relpath(file_path, directory))
    print(f"Created '{output_zip}' with files from '{directory}' excluding {exclusions}.")

def wpet():
    print('Welcome To "Export Theme" Method 😊😊😊\n')
    hmn2 = True
    while hmn2:
        theme_path = input('Please Enter Theme Path: ')
        if len(theme_path) != 0:
            if os.path.isdir(theme_path):
                if os.path.isfile(os.path.join(theme_path, 'index.php')) and \
                   os.path.isfile(os.path.join(theme_path, 'functions.php')) and \
                   os.path.isfile(os.path.join(theme_path, 'style.css')):
                    print('Processing...')
                    if os.path.isfile(os.path.join(theme_path, 'indev_ignore_file.json')):
                        print('Extracting data from "indev_ignore_file.json"')
                        with open(os.path.join(theme_path, 'indev_ignore_file.json'), 'r', encoding='utf-8') as json_file:
                            ignore = json.load(json_file)
                        zip_directory_with_exclusions(directory=theme_path, exclusions=ignore)
                    else:
                        print('No "indev_ignore_file.json" File.')
                        zip_directory_with_exclusions(directory=theme_path, exclusions=[])
                else:
                    print('This theme is incomplete and not suitable for extraction 🙂🙂🙂.')
                hmn2 = False
            else:
                print(f"The path '{theme_path}' is not a valid directory.")
        else:
            print('Unexpected Inputs !!')
