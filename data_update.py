import insta
import os
import time


username = input('enter user : ')
path = os.getcwd() + '\\' + username + '.txt'
if not os.path.exists(path):
    with open(username+'.txt', 'w') as f:
        print('Create new data user')
while 1:
    insta.writedata(insta.current_date(),username)
    time.sleep(300)
