    # Exercise:
#	* Create a login application, that can store and handle multiple users.
#	* The user should be asked if he wants to log in or create a login.
#	* If 'create': The users credentials should be written to a file
#	* If 'login': The users information should be checked agains the content of the file. 
#	* The user should be granted or denied acces. 
#
# Go for the simplest, easiest, fast approach!
#
# Most of what you need we already covered, the rest is easy
# You get 10 min. 
# Then we do it together

import sys

q = input('Do you want to create a user? (y/n)')
if q == 'y':
    username = input('Username: ')
    password = input('Password: ')
    f = open('logins.txt', 'a+')
    f.write(f'{username},{password};')
    f.close()
username = input('Username: ')
password = input('Password: ')
 
f = open('logins.txt', 'r')
res = f.read()
res = res.split(';') 
res = res[:-1] # remove last 'empty' element

for i in res:
    if i[:2] == username and i[-2:] == password:
        print('You are in!')
        sys.exit()

print('No no!')

