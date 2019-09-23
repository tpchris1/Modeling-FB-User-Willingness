
def read_url():
    f = open('read_file/user_url.txt','r')

    url = []
    url = f.readlines()
    temp = []

    for i in url:
        temp.append( i[:-1] )
    return temp

def read_ID():
    f = open('read_file/NegativeList.txt','r')

    url = []
    # url = f.readlines()
    url = f.read().splitlines()    # delete '\n'
    temp = []

    for i in url:
        temp.append( i[:] )
    return temp
