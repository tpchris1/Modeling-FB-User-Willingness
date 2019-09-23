from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import random
import time
import codecs
import read_file.read
import re
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

global id_list
id_list = read_file.read.read_ID()

def fb_More_check(browser):
    print("\nMore: Check-Ins")
    w_check = codecs.open("data/More_Check.txt",'w','utf-8-sig')
    for index, userID in enumerate(id_list):
        print(index, userID)
        userUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk=map"
        browser.get(userUrl)
        time.sleep(random.randint(3,7))
        name = []
        href = []
        soup = BeautifulSoup(browser.page_source,"html.parser")
        if (isinstance(soup.find(class_="_4-y-"), type(None)) and (not isinstance(soup.find(class_="_51sx"), type(None)))):
            last_height = browser.execute_script("return document.body.scrollHeight")
            while(True):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randint(3,7))
                new_height = browser.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            soup = BeautifulSoup(browser.page_source,"html.parser")
            for i in soup.find(class_="_5h60 _30f").find_all(class_="_gx7"):
                name.append(i.get_text())
                href.append(i['href'])
            for i,h in enumerate(href): # Derive ID in this for-loop
                print(userID,i,h)
                if not h[0]=='h': # this chek-in is an event, not pages
                    IDtemp = []
                    for m in re.finditer('(?=/)', h): ## get event ID from event url
                        IDtemp.append(m.start())
                    ID = h[IDtemp[1]+1:IDtemp[2]]
                else: # this check-in is a pages, then we go to the pages to get page ID
                    if(h.find("https://www.facebook.com/pages/")==0): # we can get ID directly from href
                        for m in re.finditer('(?=/)', h):
                            IDbegin = m.start()
                        ID = h[IDbegin+1:]
                    else: # we have to go to this page to get ID
                        browser.get(h)
                        time.sleep(random.randint(3,7))
                        soup = BeautifulSoup(browser.page_source,"html.parser")
                        if (isinstance(soup.find(class_="_2yav"), type(None))): # get page ID from old_page format
                            ID = soup.find(class_="_5ss8").find('div').find('div')['id']
                            ID = str(ID[ID.find('_')+1:])
                        else: # get page ID from new_page format
                            ID = soup.find("meta",  property="al:android:url")["content"]
                            ID = ID[ID.find('page')+5:ID.find('?')]
                w_check.write(userID + " \"\" " + name[i] + " \"\" " + ID + "\n")
        else:
            w_check.write(userID + " \"\" Empty" + " \"\" Empty\n")
    w_check.close()

def fb_More_like(browser):
    print("\nMore: Likes")
    w_like = codecs.open("data/More_Like.txt",'w','utf-8-sig')
    for index, userID in enumerate(id_list):
        print(index, userID)
        userUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk=likes"
        browser.get(userUrl)
        time.sleep(random.randint(3,7))
        soup = BeautifulSoup(browser.page_source,"html.parser")
        if not (isinstance(soup.find(class_="_3i9"), type(None))):
            last_height = browser.execute_script("return document.body.scrollHeight")
            while(True):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randint(3,7))
                new_height = browser.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            soup = BeautifulSoup(browser.page_source,"html.parser")
            for i in soup.find(class_="_3i9").find_all(class_="clearfix _5t4y _5qo4"):
                name = i.find(class_="fsl fwb fcb").get_text()
                ID = i.find(class_="fsl fwb fcb").find('a').get('data-hovercard')
                ###AttributeError: 'NoneType' object has no attribute 'find'
                ID = ID[ID.find('?id=')+4:]
                category = i.find(class_="fsm fwn fcg").get_text()
                w_like.write(userID + " \"\" " + name + " \"\" " + ID + " \"\" " + category + "\n")
        else:
            w_like.write(userID + " \"\" Empty" + " \"\" Empty" + " \"\" Empty\n")
