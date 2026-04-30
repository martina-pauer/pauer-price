#!/usr/bin/python3
import os
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

select: str = input('\nDo You Want Run All The Apps? Y/n: ').lower()
prefix: str = '/workspaces/pauer-price/src/'

if select == 'n': 
    # Ask for web app to run    
    select: str = input('\nWrite option number: ')
    # Run selected option to Flask Web App
    os.system(f'flask --app {options[int(select) - 1]} run')
    # Delete uneeded data
    del select
    try:
        # Automatically clean cache when the app was already has been used
        os.system(f'rm -R {prefix}__pycache__')
        os.system(f'rm -R {prefix}mods/__pycache__')
        del prefix
    except:
        pass
    del os
else:
    del select
    # Run all apps loading each name and when is needed clean cache
    for app in options:
        os.system(f'flask --app {app} run')
        try:
            # Automatically clean cache after each run
            os.system(f'rm -R {prefix}__pycache__')
            os.system(f'rm -R {prefix}mods/__pycache__')
            del prefix
        except:
            pass
    del os