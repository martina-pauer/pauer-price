#!/usr/bin/python3
import os
import sys
# Change Automaticly the encryption for security reasons in encypter source 'encrypt.json'
os.system('cd web && chmod +x encrypt_gen.py && ./encrypt_gen.py && cd ..')
# Automatation interactive script for run all the web app or only of them
options: list[str] =    [
                            'tango'
                        ]

print('Run one or all this web apps with API integrations\n')
count: int = 1
# Show each web app option to the administrator
for option in options:
    print(f'\t{count}) {option}\n')
    count += 1
# Delete variable for save RAM
del count   

if sys.argv.__len__() == 1:
    select: str = input('\nDo You Want Run All The Apps? Y/n: ').lower()
elif sys.argv.__len__() == 3:
    # Get how much web app run
    select: str = sys.argv[sys.argv.index('--run_all') + 1].replace(' ', '')
else:
    select: str = 'n'    

prefix: str = '/workspaces/pauer-price/src/'

if select == 'n': 
    # Ask for web app to run
    if sys.argv.__len__() != 5:    
        select: str = input('\nWrite option number: ')
    elif sys.argv.__len__() == 5:
        select: str = sys.argv[sys.argv.index('--selected_app') + 1].replace(' ', '')      
    select: int = int(select)    
    # Run selected option to Flask Web App
    if ((select > 0) and ((select - 1) <= options.__len__())):
        os.system(f'flask --app {options[select - 1]} run')
        try:
            # Automatically clean cache when the app was already has been used
            os.system(f'rm -R {prefix}__pycache__')
            os.system(f'rm -R {prefix}mods/__pycache__')
        except:
            pass
    else:
        print(f'Option {select} for web app doesn\'t exist')
    # Delete uneeded data
else:   
    # Run all apps loading each name and when is needed clean cache
    for app in options:
        os.system(f'flask --app {app} run')
        try:
            # Automatically clean cache after each run
            os.system(f'rm -R {prefix}__pycache__')
            os.system(f'rm -R {prefix}mods/__pycache__')
        except:
            pass
    del prefix 
del select, os, sys