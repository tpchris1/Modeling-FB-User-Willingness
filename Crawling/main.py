from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup

import about.about as abt
import more.more as more
import read_file.read
import friendlist.friendlist as fl
import random
import time
import datetime
import codecs
import re

global id_list
id_list = read_file.read.read_ID()

def fb_login():
    global browser
    browser = webdriver.Chrome()
    #browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    browser.get("https://www.facebook.com/?locale=en_US")
    
    #user credentials
    user = browser.find_element_by_id("email")
    password = browser.find_element_by_id('pass')
    
    user.send_keys('************@gmail.com')
    password.send_keys('********')
    
    time.sleep(10)
    browser.find_element_by_id("loginbutton").click()
    print ("login")
    time.sleep(10)

def fb_getUserID(userUrl):
    browser.get(userUrl)
    while (True):
        try:
            aboutme = browser.find_element_by_link_text("About").click()
            break
        except NoSuchElementException as e:
            browser.refresh()
            time.sleep(1)
            pass
    l=[]
    for m in re.finditer("%3A",browser.current_url):
        l.append(m.start())
        l.append(m.end())
    return browser.current_url[l[1]:l[2]]

def fb_Timeline(userID):
    userUrl = "https://www.facebook.com/profile.php?id=" + userID
    browser.get(userUrl)
    time.sleep(10)
    count=0
    while (count < 2):
        try:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)
            count = count + 1
        except WebDriverException as e:
            browser.refresh()
            time.sleep(10)
            count = 0
            print ("Refresh")
    
    #soup = BeautifulSoup(browser.page_source,"html.parser")
    time.sleep(10)
    try:
        a = browser.find_elements_by_class_name("UFIPagerLink")
        b = browser.find_elements_by_class_name("UFIReplySocialSentenceLinkText")
    except StaleElementReferenceException as err:
        pass
    
    for i in a:
        #i.click()
        browser.execute_script("arguments[0].click();", i)
    for i in b:
        browser.execute_script("arguments[0].click();", i)
    
    time.sleep(10)
    soup = BeautifulSoup (browser.page_source,"html.parser")
    posts = soup.find_all(class_= '_4-u2 mbm _4mrt _5jmm _5pat _5v3q _4-u8')
    
    for i in posts:
        #Post Time
        post_time = i.find(class_='_5ptz')['title']
        print(post_time)
        
        #Poster
        poster = i.find(class_="fwb").get_text()
        print(poster)
        
        #Status
        status = i.find(class_="fcg").get_text()
        try:
            print(status[len(poster)+1:])
        except AttributeError as e:
            print("")
        
        #place
        place = i.find(class_="fcg").find_all(class_="profileLink")
        try:
            print(place[1]['href'])
            print(place[1].get_text())
        except TypeError as e1:
            pass
        except IndexError as e2:
            pass
        
        #Post Content
        content = i.find(class_='_5pbx')
        print("Post:")
        if ( isinstance(content, type(None)) ): #no post content
            print ("")
        else:
            usercontent = content.find(class_='text_exposed_root')
            if( isinstance(usercontent, type(None)) ): #no "See More"
                try:
                    print(content.get_text())
                except UnicodeEncodeError as e:
                    print ("emoji")
            else: #There is "See More"
                try:
                    print(usercontent.find('p').get_text())
                    remain_post = usercontent.find('div',{'class':'text_exposed_show'})
                    if not( isinstance(remain_post, type(None)) ):
                        print (remain_post.get_text())
                except UnicodeEncodeError as e:
                    print ("emoji")
        
        #Post Likes
        likes = i.find(class_='_1g5v')
        if ( isinstance(likes, type(None)) ):
            print ("likes:0")
        else:
            print ("likes:",likes.get_text())
        
        #Post Comment
        print ("Comment:")
        comment = i.find_all(class_='UFICommentContentBlock')
        if ( isinstance(comment, type(None)) ): #no comment content
            print ("")
        else:
            for c in comment:
                comment_actor = c.find(class_='UFICommentActorName').get_text()
                comment_time = c.find(class_='livetimestamp')['title']
                comment_content = c.find(class_='UFICommentBody').get_text()
                sticker = c.find(class_='UFICommentContent').find('div')
                if not ( isinstance(sticker, type(None)) ):
                    try:
                        print (sticker['style'])
                    except KeyError as e:
                        try:
                            print (sticker.find('a')['data-ploi'])
                        except KeyError as ee:
                            pass
                try:
                    print(comment_actor,comment_content,comment_time)
                except UnicodeEncodeError as e:
                    print ("emoji",comment_time)
        print("----------------------------------")

def fb_More_section(userID,section,userUrl):
    sectionUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk="+section
    browser.get(sectionUrl)
    time.sleep(5)
    if(browser.current_url==userUrl):
        print("Hide")
    else:
        soup = BeautifulSoup (browser.page_source,"html.parser")
        if (soup.find(class_="_4-y-")):
            print ("Empty")
        else:
            if(section == "map"):
                count = 0
                while (count < 10):
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(0.2)
                    try:
                        browser.find_element_by_xpath("//*[@id='timeline-medley']/div/div[2]/div[1]/div/div/h3")
                        break
                    except NoSuchElementException as e:
                        count = count + 1
                        print(count)
                        pass
            else:
                last_height = browser.execute_script("return document.body.scrollHeight")
                while(True):
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(random.randint(3,7))
                    new_height = browser.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        break
                    last_height = new_height
                """while True :
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(0.2)
                    try:
                            browser.find_element_by_xpath("//*[@id='timeline-medley']/div/div[2]/div[1]/div/div/h3")
                            break
                    except NoSuchElementException as e:
                            pass"""
            soup = BeautifulSoup (browser.page_source,"html.parser")
            content = soup.find_all(class_="_gx7")
            for i in content:
                print(i.get_text())
                print(i['href'])
    print("-------------------------------------")

def fb_More_Group(userID,section,userUrl,class_name):
    GroupUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk="+section
    browser.get(GroupUrl)
    time.sleep(5)
    if(browser.current_url==userUrl):
        print("Hide")
    else:
        soup = BeautifulSoup (browser.page_source,"html.parser")
        if (soup.find(class_="_4-y-")):
            print ("Empty")
        else:
            last_height = browser.execute_script("return document.body.scrollHeight")
            while(True):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randint(3,7))
                new_height = browser.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            """while True:
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(0.2)
                try:
                        browser.find_element_by_xpath("//*[@id='timeline-medley']/div/div[2]/div[1]/div/div/h3")
                        break
                except NoSuchElementException as e:
                        pass"""
            
            soup = BeautifulSoup (browser.page_source,"html.parser")
            content = soup.find_all(class_=class_name)
            if (section=="events"):
                for i in content:
                    print(i.find('a')['href'])
                    print(i.find('a').get_text())
                    print(i.find('div').get_text())
            
            elif (section=="groups" or "likes"):
                for i in content:
                    print(i.get_text())
                    print(i.find('a')['href'])
            else:
                for i in content:
                    reviewUrl = i.find(class_="fwb")
                    print(reviewUrl.get_text())
                    print(reviewUrl.find('a')['href'])
                    star = i.find(class_="_2u7k")
                    try :
                        print(star.get_text())
                    except AttributeError as e:
                        print("Empty")
                    
                    review_time = i.find(class_="_39g5")
                    print(review_time.find('abbr')['title'])
                    print(i.find(class_="_5mu1").get_text())

    print("-------------------------------------")



def fb_More(userID):
        userUrl = "https://www.facebook.com/profile.php?id="+userID
        browser.get(userUrl)
        time.sleep(5)
        userUrl = browser.current_url

        ##print("Videos ************")
        ##
        print("Check-in")
        fb_More_section(userID,"map",userUrl)
        print("Sports")
        fb_More_section(userID,"sports",userUrl)
        print("Music")
        fb_More_section(userID,"music",userUrl)
        print("Movies")
        fb_More_section(userID,"movies",userUrl)
        print("TV")
        fb_More_section(userID,"tv",userUrl)
        print("Books")
        fb_More_section(userID,"books",userUrl)
        print("Games")
        fb_More_section(userID,"games",userUrl)
        print("Likes")
        fb_More_Group(userID,"likes",userUrl,"fsl fwb fcb")
        print("Events")
        fb_More_Group(userID,"events",userUrl,"_4cbv")##
        print("Reviews")
        fb_More_Group(userID,"reviews",userUrl,"_5mt_")##
        # print("Groups")
        # fb_More_Group(userID,"groups",userUrl,"mbs fwb")

def fb_Post(browser):
    for index, userID in enumerate(id_list):
        w_post = codecs.open("data/data_post.txt",'a','utf-8-sig')
        w_flcnt = codecs.open("data/data_friendsCNT.txt",'a','utf-8-sig')
        print(index, userID)
        userUrl = "https://www.facebook.com/profile.php?id=" + userID
        
        browser.get(userUrl)
        time.sleep(10)
        posts_count = 0
        less_than_year = True
        posts = []
        #last_height = browser.execute_script("return document.body.scrollHeight")
        
        while(posts_count < 20 or less_than_year):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randint(3,10))
            try:
                soup = BeautifulSoup (browser.page_source, "html.parser")
            except:
                browser.refresh()
                print('soup error')
                posts_count = 0
                less_than_year = True
                posts = []
                soup = BeautifulSoup (browser.page_source, "html.parser")
            posts = soup.find_all(class_= '_5pcb _4b0l _2q8l')
            posts_count = len(posts)
            #new_height = browser.execute_script("return document.body.scrollHeight")
            
            bottom = soup.find(class_='img sp_Bclo982F-vA sx_ba01a2')
            
            """
            if new_height == last_height:   # 無更多貼文
                print('no more posts.')
                break
            """
            if str(bottom) != 'None':   # 無更多貼文
                print('no more posts.')
                break
            else:
                #last_height = new_height
                if posts_count >= 20:
                    for idx, p in enumerate(posts):
                        #檢查有沒有非貼文的 element
                        if 'Posts from' in p.get_text():
                            posts_count = posts_count - 1
                        else:
                            pass
                    #if posts_count >= 20:
                        
                for p in reversed(posts):
                    if 'Posts from' in p.get_text():
                        pass
                    else:
                        try:
                            last_post_time = p.find(class_='_5ptz')['title']
                            date = last_post_time.split('/')
                            post_mon = int(date[0])
                            post_mday = int(date[1])
                            post_year = int(date[2].split(',')[0])
                            if post_year < 59:
                                post_year = 2000 + post_year
                            else:
                                post_year = 1900 + post_year
                            
                            days = str(datetime.date.today() - datetime.date(post_year, post_mon, post_mday)).split(' ')[0]
                            if days == '0:00:00':
                                days = 0
                            if int(days) >= 180 and less_than_year:   # 爬文達到一年
                                print('arrive one year')
                                #print(p.get_text())
                                less_than_year = False
                            break
                        except:
                            pass
                    
        post_time_10th = ''
        post_time_20th = ''
        post_time_1year = ''
        post_shared_count = 0
        post_notshared_count = 0
        post_year_count = 0
        post_public_10 = 'False'
        post_public_20 = 'False'
        break_year = False
        break_10 = False
        break_20 = False
        days = 0
        
        for idx, p in enumerate(posts):
            if 'Posts from' in p.get_text():
                pass
            else:
                print('index: ' + str(idx))
                try:
                    post_time = p.find(class_='_5ptz')['title']
                    try:
                        post_href = p.find(class_='_5pcq')['href']
                        if 'https://' not in post_href:
                            post_href = 'https://www.facebook.com' + post_href
                        print(post_href)
                    except:
                        #print('no href\n')
                        pass
                    #Post Time
                    try:
                        post_title = p.find(class_='fcg').get_text()
                        post_name = p.find(class_='fwb').get_text()
                        #print('post_title: ' + post_title)
                        #print('post_name: ' + post_name)
                        post_title = post_title.replace(post_name, '')
                        #print('post_title: ' + post_title)
                        share = post_title.split(' ')[1]
                        #print(share)
                        if share == 'shared':
                            #print('this is shared post')
                            post_shared_count = post_shared_count + 1
                        else:
                            post_notshared_count = post_notshared_count + 1
                    except:
                        post_notshared_count = post_notshared_count + 1
                    
                    #print(post_time + '\n')
                    date = post_time.split('/')
                    post_mon = int(date[0])
                    post_mday = int(date[1])
                    post_year = int(date[2].split(',')[0])
                    
                    if post_year < 59:
                        post_year = 2000 + post_year
                    else:
                        post_year = 1900 + post_year
                    
                    timestamp = date[2].split(',')[1].split(' ')
                    post_hour = timestamp[1].split(':')[0]
                    post_min = timestamp[1].split(':')[1]
                    if timestamp[2] == 'AM' and post_hour == '12':
                        post_hour = str(int(post_hour) - 12)
                    if timestamp[2] == 'PM' and post_hour != '12':
                        post_hour = str(int(post_hour) + 12)
                    #print(post_mon + ' ' + post_mday + ' ' + post_year)
                    #print(post_hour + ' ' + post_min)
                    #print(timestamp)
                    #Post href
                    
                    days = str(datetime.date.today() - datetime.date(post_year, post_mon, post_mday)).split(' ')[0]
                    if days == '0:00:00':
                        days = 1
                    else:
                        days = int(days) + 1
                    if int(days)<= 180:
                        post_year_count = post_year_count + 1
                    else:
                        break_year = True
                    
                    
                    #Poster
                    try:
                        post_message = p.find("div", {"data-testid" : "post_message"}).find("p").get_text()
                        #print(post_message)
                    except:
                        pass
                except:
                    pass
            #print('post_shared_count:' + str(post_shared_count))
            #print('post_notshared_count:' + str(post_notshared_count))
            if (post_shared_count + post_notshared_count) == 10 and not break_10:
                post_time_10th = post_time
                #print('post_time_10th:' + post_time_10th)
                post_public_10 = 'True'
                post_shared_proportion_10 = post_shared_count / 10
                post_frequency_10 = 10 / int(days)
                post_period_10 = int(days) / 10
                break_10 = True
            if (post_shared_count + post_notshared_count) == 20 and not break_20:
                post_time_20th = post_time
                #print('post_time_20th:' + post_time_20th)
                post_public_20 = 'True'
                post_shared_proportion_20 = post_shared_count / 20
                post_frequency_20 = 20 / int(days)
                post_period_20 = int(days) / 20
                break_20 = True
            if break_year and break_20:
                break
            
            print("----------------------------------")
            
        if (post_shared_count + post_notshared_count) == 0:
            post_shared_proportion_10 = 0
            post_frequency_10 = 0
            post_shared_proportion_20 = 0
            post_frequency_20 = 0
        else:
            if not break_10:
                post_shared_proportion_10 = post_shared_count / (post_shared_count + post_notshared_count)
                post_frequency_10 = (post_shared_count + post_notshared_count) / int(days)
            if not break_20:
                post_shared_proportion_20 = post_shared_count / (post_shared_count + post_notshared_count)
                post_frequency_20 = (post_shared_count + post_notshared_count) / int(days)
        """
        days = str(datetime.date.today() - datetime.date(post_year, post_mon, post_mday)).split(' ')[0]
        if days == '0:00:00':
            days = 0
        post_period_20 = int(days) / (post_shared_count + post_notshared_count)
        """
        w_post.write(userID + " \"\" " + post_public_10 + " \"\" " + str(post_shared_proportion_10) + " \"\" " + str(post_frequency_10) + " \"\" "  + post_public_20 + " \"\" " + str(post_shared_proportion_20) + " \"\" " + str(post_frequency_20) + " \"\" " + str(post_year_count) + "\n")
        
        # FRIEND COUNT
        """
        userUrl = "https://www.facebook.com/profile.php?id=" + userID
        
        browser.get(userUrl)
        time.sleep(10)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        soup = BeautifulSoup(browser.page_source,"html.parser")
        """
        try:
            friend_count = soup.find(class_="_50f8 _2iem").get_text()
            friend_count = friend_count.replace(',', '')
            
        except:
            friend_count = 'Empty'
        print('friend_count: ' + friend_count)
        w_flcnt.write(userID + " \"\" " + friend_count +"\n")
        w_post.close()
        w_flcnt.close()
#Start crawling
"""
fb_login()

abt.fb_About_all(browser)

abt.fb_About_edu(browser)

abt.fb_About_living(browser)

abt.fb_About_info(browser)

abt.fb_About_rela(browser)
        
abt.fb_About_bio(browser)

abt.fb_About_life(browser)

more.fb_More_check(browser)

more.fb_More_like(browser)

fl.fb_getFriends(browser)

fl.fb_Friends_Count(browser)

fb_Timeline("4")

fb_More("4")
"""
#fb_Post("100002725621522")
fb_Post(browser)

print("Done")
#browser.close()
