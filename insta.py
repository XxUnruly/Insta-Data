from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import datetime


def find_data(bigdata,index,littledata):
    i = index + len(littledata)
    nbr = ''
    while bigdata[i].isdigit():
        nbr += str(bigdata[i])
        i += 1
    return nbr


def recupAbos(username):
    link = 'https://www.instagram.com/'+username+'/'
    requete = requests.get(link)
    page = requete.content
    soup = BeautifulSoup(page, "html.parser")
    p = soup.find_all('script')
    data = str(p[3])
    a = data.find('edge_followed_by":{"count":')
    b = data.find('edge_follow":{"count":')
    followed = find_data(data,a,'edge_followed_by":{"count":')
    follow = find_data(data,b,'edge_follow":{"count":')
    return [int(followed),int(follow)]

    
def clcl_ratio(followers, following):
    try:
        return round(following/followers,2)
    except ZeroDivisionError:
        return 0

    
def current_date():
    return str(datetime.datetime.now()).replace(" ", "")


def writedata(date, username):
    try:
        with open(username+'.txt', 'a') as f:
            f.write(date + ' ' + str(recupAbos(username)[0]) + ' ' + str(recupAbos(username)[1]) + ' ' + str(clcl_ratio(recupAbos(username)[0], recupAbos(username)[1])) + '\n')
            print('data update')
    except:
        with open(username+'.txt', 'a') as f:
            f.write(date + ' ' + str(recupAbos(username)[0]) + ' ' + str(recupAbos(username)[1]) + ' ' + str(clcl_ratio(recupAbos(username)[0], recupAbos(username)[1])) + '\n')
            print('data update')


def read_data(username):
    with open(username+'.txt', 'r') as f:   
        contenu = f.read()
    a = contenu.split('\n')
    if '' in a:
        a.remove('')
    data = []
    for obj in a:
        b = obj.split(' ')
        data.append(b)
    return data


def create_graphe(data):
    date = []
    followers = []
    following = []
    ratio = []
    for obj in data:
        date.append(obj[0])
        followers.append(int(obj[1]))
        following.append(int(obj[2]))
        ratio.append(float(obj[3]))

    plt.style.use('Solarize_Light2')

    plt.subplot(3, 1, 1)
    plt.plot(date,followers, label="Followers", color='b', linewidth=0.8 )
    plt.grid(True)
    plt.title("Followers evolution")
    plt.xticks([])
    plt.legend() 
    
    plt.subplot(3, 1, 2)
    plt.plot(date,following, label="Following", color='m', linewidth=0.8)
    plt.grid(True)
    plt.title("Following evolution")
    plt.xticks([])
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(date,ratio, label="Ratio", color='y', linewidth=0.8)
    plt.grid(True)
    plt.title("Ratio evolution")
    plt.xticks([])
    plt.legend()

    plt.savefig('fig.png', bbox_inches='tight')
    plt.show()
