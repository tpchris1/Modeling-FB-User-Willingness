import time
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import random
import codecs
import read_file.read

global id_list
id_list = read_file.read.read_ID()

def fb_getFriends(browser):
    print("\nFriends:")
    w = codecs.open("data/data_friendlist.txt",'w','utf-8-sig')
    for index, userID in enumerate(id_list):
        print(index, userID)
        print("check point1")
        userUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk=friends"
        browser.get(userUrl)
        time.sleep(random.randint(5,12))
        friendlist = []
        #name = []
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randint(5,10))
        soup = BeautifulSoup (browser.page_source,"html.parser")
        friend_ststus = soup.find(class_="_3sz")
        no_element = soup.find(class_="_4-y-")
        if (isinstance(no_element, type(None)) ):
            try:
                if ((friend_ststus.get_text() =="Following") or (friend_ststus.get_text()=="Followers")):
                    w.write(userID + " , Empty\n")
                    print("check point2-1")
                else:
                    browser.refresh()
                    time.sleep(random.randint(5,12))
                    time.sleep(random.randint(3,7))
                    scroll_count = 0
                    loop_count = 0
                    print("check point2-2")
                    while (True):
                        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        #delay = input("scroll to bottom by hand and then type any to resume: ")
                        time.sleep(random.randint(3,8))
                        scroll_count = scroll_count + 1
                        try:
                            browser.find_element_by_xpath("//*[@id='timeline-medley']/div/div[2]/div[1]/div/div/h3")
                            print("check point3")
                            break
                        except NoSuchElementException as e:
                            pass
                        if scroll_count == 1000:
                            browser.refresh()
                            loop_count = loop_count +1
                        elif loop_count == 10:
                            return False

                    soup = BeautifulSoup (browser.page_source,"html.parser")
                    div_lotstars = soup.find_all('li', {'class': '_698'})
                    print("check point4")
                    for i in div_lotstars:
                        friend = i.find(class_="fsl")
                        #name.append(friend.find('a').get_text())
                        friend_name = friend.find('a').get_text()
                        temp = friend.find('a').get('data-gt')
                        if not ( isinstance(temp, type(None)) ):
                            IDbegin = temp.find("\"eng_tid\":")+11  #find the begin of id in temp
                            IDend = temp.find("\"",IDbegin )
                            friendID = temp[IDbegin:IDend]
                            w.write(userID+", "+friend_name + ", " + friendID + "\n")
                            #w.write(friendID + "\n")
                            #if not friendID in origin_id:
                            #        friendlist.append(friendID)
                    print("check point5")
                    time.sleep(random.randint(5,12))
            except AttributeError:
                w.write(userID+" , "+"Empty\n")
        else:
            w.write(userID+" , "+"Empty\n")
        #return True
#### true / false is 沒有意義 now

def fb_Friends_Count(browser):
    print("\nFriends: Count")
    # Work & Education
    w_flcnt = codecs.open("data/data_friendsCNT.txt",'w','utf-8-sig')
    for index, userID in enumerate(id_list):
        print(index, userID)
        userUrl = "https://www.facebook.com/profile.php?id=" + userID
        
        browser.get(userUrl)
        time.sleep(7)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        
        soup = BeautifulSoup(browser.page_source,"html.parser")
        try:
            friend_count = soup.find(class_="_50f8 _2iem").get_text()
            friend_count = friend_count.replace(',', '')
            
        except:
            friend_count = 'Empty'
        print(friend_count)
        w_flcnt.write(userID + " \"\" " + friend_count +"\n")
    
    w_flcnt.close()
    