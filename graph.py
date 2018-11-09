import insta
import os


username = input('enter user : ')
path = os.getcwd() + '\\' + username + '.txt'
if os.path.exists(path):
    insta.create_graphe(insta.read_data(username))
else:
    print("No data")
