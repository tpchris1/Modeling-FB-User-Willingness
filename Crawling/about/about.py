from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import random
import time
import codecs
import read_file.read

global id_list
global w
id_list = read_file.read.read_ID()

global delay
delay = 5


def fb_About_all(browser):
    print("\nAbout: All")
    # Work & Education
    w_work = codecs.open("data/data_work.txt",'w','utf-8-sig')
    w_proskill = codecs.open("data/data_proskill.txt",'w','utf-8-sig')
    w_edu = codecs.open("data/data_edu.txt",'w','utf-8-sig')
    # Places He/She's Lived
    w_CCH = codecs.open("data/data_CCH.txt",'w','utf-8-sig')     # CURRENT CITY AND HOMETOWN
    w_OPL = codecs.open("data/data_OPL.txt",'w','utf-8-sig')     # OTHER PLACES LIVED
    # Contact and Basic Info
    w_mob = codecs.open("data/data_mob.txt",'w','utf-8-sig')
    w_add = codecs.open("data/data_add.txt",'w','utf-8-sig')
    w_email = codecs.open("data/data_email.txt",'w','utf-8-sig')
    w_fb = codecs.open("data/data_fb.txt",'w','utf-8-sig')
    w_web = codecs.open("data/data_web.txt",'w','utf-8-sig')
    w_link = codecs.open("data/data_link.txt",'w','utf-8-sig')
    w_info = codecs.open("data/data_info.txt",'w','utf-8-sig')
    w_lan = codecs.open("data/data_lan.txt",'w','utf-8-sig')
    # Family and Relationships
    w_rela = codecs.open("data/data_rela.txt",'w','utf-8-sig')
    w_fam = codecs.open("data/data_fam.txt",'w','utf-8-sig')
    # Details About Him/Her
    w_detail = codecs.open("data/data_detail.txt",'w','utf-8-sig')
    w_other = codecs.open("data/data_other.txt",'w','utf-8-sig')
    # Life Events
    w_life = codecs.open("data/data_life.txt",'w','utf-8-sig')
    #############################################################
    for index, userID in enumerate(id_list):
        print(index, userID)
        userUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk=about&section=education"
        browser.get(userUrl)
        # Work & Education ######################################
        time.sleep(random.randint(7,16)) ### Wait for 7 - 16 seconds
        soup = BeautifulSoup(browser.page_source,"html.parser")
        b_work = b_edu = b_proskill = False
        if not (isinstance(soup.find(class_="_4qm1"), type(None)) ): ### check to pass the user or not
            for i in soup.find_all(class_="_4qm1"):
                blockname = i.find('div').get_text()  ### 2 block for Work + Edu / ProSkill
                if not(isinstance(i.find(class_="_43c8 _5f6p fbEditProfileViewExperience experience"), type(None) )):
                    if not(blockname=="Professional Skills"):
                        if(blockname=="Work"):
                            b_work = True
                            w = w_work
                        elif(blockname=="Education"):
                            b_edu = True
                            w = w_edu
                        else:
                            print("error occured")
                        for work in i.find_all(class_="_43c8 _5f6p fbEditProfileViewExperience experience"):
                            work_name = work.find(class_="_2lzr _50f5 _50f7")
                            work_ID = work_name.find('a')['data-hovercard']
                            w.write(userID + " \"\" " + work_name.get_text() + " \"\" " + work_ID[work_ID.find("id=")+3:])
                            work_b1 = work.find(class_="fsm fwn fcg")
                            if( isinstance(work_b1, type(None)) ):
                                w.write(" \"\" Empty")
                            else:
                                w.write(" \"\" " + work_b1.get_text())
                            if not(isinstance(work.find(class_="_5mqb"), type(None))):
                                work_b2 = work.find(class_="_5mqb") # class error-->"_6a _6b"
                            else:
                                work_b2 = work.find(class_="_3-8w _50f8")
                            if( isinstance(work_b2, type(None)) ):
                                w.write(" \"\" Empty\n")
                            else:
                                w.write(" \"\" " + work_b2.get_text()+"\n")
                    else: ### ProSkill
                        b_proskill = True
                        for skill in i.find_all(class_="_3l7z _39g6"):
                            skill_name = skill.get_text()
                            skill_ID = skill['data-hovercard']
                            w_proskill.write(userID + " \"\" " + skill_name + " \"\" " + skill_ID[skill_ID.find("id=")+3:]+"\n")

            if not(b_work):
                w_work.write(userID + " \"\" Empty \"\" Empty \"\" Empty \"\" Empty\n")
            if not(b_proskill):
                w_proskill.write(userID + " \"\" Empty \"\" Empty\n")
            if not(b_edu):
                w_edu.write(userID + " \"\" Empty \"\" Empty \"\" Empty \"\" Empty\n")
        # Places He/She's Lived ######################################
        browser.find_element(By.XPATH, "//*[@class='_5pwr _Interaction__ProfileSectionPlaces']").click();
        time.sleep(random.randint(3,8)) ### Wait for 7 - 16 seconds
        soup = BeautifulSoup(browser.page_source,"html.parser")
        b_OPL = False12
        if not (isinstance(soup.find(class_="_4qm1"), type(None)) ): ### check to pass the user or not
            for i in soup.find_all(class_="_4qm1"):
                blockname = i.find('div').get_text() ### 2 bolcks for Current City + Hometown/Other Place Lived
                if (blockname=="Current City and Hometown"):
                    place = i.find_all(class_="_3pw9 _2pi4 _2ge8")
                    CC_name = CC_ID = HT_name = HT_ID = "Empty"
                    for j in place:
                        if( isinstance(j.find(class_="_2iel _50f7"), type(None)) ):
                            w_CCH.write(userID + " \"\" Empty" + " \"\" Empty" + " \"\" Empty" + " \"\" Empty\n")
                        else:
                            if(j.find(class_="fsm fwn fcg").get_text()=="Current city"):
                                CC = j.find(class_="_2iel _50f7")
                                CC_name = CC.get_text()
                                if not(isinstance(CC.find('a'), type(None))):
                                    CC_ID = CC.find('a')['data-hovercard']
                                CC_ID = CC_ID[CC_ID.find("id=")+3:]
                            elif(j.find(class_="fsm fwn fcg").get_text()=="Hometown"):
                                HT = j.find(class_="_2iel _50f7")
                                HT_name = HT.get_text()
                                if not(isinstance(HT.find('a'), type(None))):
                                    HT_ID = HT.find('a')['data-hovercard']
                                HT_ID = HT_ID[HT_ID.find("id=")+3:]
                    w_CCH.write(userID + " \"\" " + CC_name + " \"\" " + CC_ID + " \"\" " + HT_name + " \"\" " + HT_ID + "\n")
                else:
                    b_OPL = True
                    for place in i.find_all(class_="_43c8 _5f6p"):
                        place_name = place.find(class_="_2iel _50f7").get_text()
                        if not(isinstance(place.find(class_="_2iel _50f7").find('a'), type(None))):
                            place_ID = place.find(class_="_2iel _50f7").find('a')['data-hovercard']
                        else:
                            place_ID = "Empty"
                        place_detail = place.find(class_="fsm fwn fcg").get_text()
                        w_OPL.write(userID + " \"\" " + place_name + " \"\" " + place_ID[place_ID.find("id=")+3:] + " \"\" " + place_detail + "\n")
        if not(b_OPL):
            w_OPL.write(userID + " \"\" Empty" + " \"\" Empty" + " \"\" Empty\n")
        # Contact and Basic Info ######################################
        browser.find_element(By.XPATH, "//*[@class='_5pwr _Interaction__ProfileSectionContactBasic']").click();
        time.sleep(random.randint(3,8)) ### Wait for 7 - 16 seconds
        soup = BeautifulSoup(browser.page_source,"html.parser")
        b_mob = b_email = b_web = b_link = False
        address = zipcode = neighborhood = fb = "Empty"
        birth = gender = blood = inter = r_name = r_id = r_detail = p_name = p_id = p_detail = "Empty"
        b_lan = False
        if not (isinstance(soup.find(class_="_4qm1"), type(None)) ): ### check to pass the user or not
            for i in soup.find_all(class_="_4qm1"):
                blockname = i.find('div').get_text() ### 3 bolcks for Contact / Website / Information
                if (blockname=="Contact Information"):
                    for j in i.find_all(class_="clearfix _ikh"):
                        section = j.find(class_="_50f4 _5kx5").get_text()
                        if(section=="Mobile Phones"):
                            b_mob = True
                            phone = j.find_all("li")
                            for p in phone:
                                w_mob.write(userID + " \"\" " + p.get_text() + "\n")
                        elif(section=="Address"):
                            address = j.find(class_="_4bl7 _pt5").get_text()
                        elif(section=="Neighborhood"):
                            neighborhood = j.find(class_="_4bl7 _pt5").get_text()
                        elif(section=="Email"):
                            b_email = True
                            email = j.find_all(class_="_50f9 _50f7")
                            for e in email:
                                w_email.write(userID + " \"\" " + e.get_text() + "\n")
                        else: #FB
                            fb = j.find(class_="_4bl7 _pt5").get_text()
                elif(blockname=="Websites and Social Links"):
                    for j in i.find_all(class_="clearfix _ikh"):
                        section = j.find(class_="_50f4 _5kx5").get_text()
                        if(section=="Websites"):
                            b_web = True
                            for web in j.find_all(class_="_39g6"):
                                w_web.write(userID + " \"\" " + web.get_text() + "\n")
                        else: #social link
                            b_link = True
                            for link in j.find_all(class_="uiList _509- _4ki _6-h _6-j _6-i"):
                                social_link = link.find_all('li')[0].get_text()
                                cate = link.find_all('li')[1].get_text()
                                w_link.write(userID + " \"\" " + social_link + " \"\" " + cate + "\n")
                else: # Basic Information
                    for j in i.find_all(class_="clearfix _ikh"):
                        section = j.find(class_="_50f4 _5kx5").get_text()
                        temp = j.find(class_="_4bl7 _pt5").get_text()
                        if(section == "Birthday"):
                            if not(temp[:8]=="Ask for "):
                                birth = temp
                        elif(section == "Gender"):
                            gender = temp
                        elif(section == "Blood Type"):
                            blood = temp
                        elif(section == "Interested In"):
                            inter = temp
                        elif(section == "Religious Views"):
                            reli = j.find(class_="uiList _4kg _6-h _704 _6-i")
                            if(isinstance(reli.find('a'), type(None))):
                                r_name = reli.get_text()
                            else:
                                r_name = reli.find('a').get_text()
                                r_id = reli.find('a')['data-hovercard']
                                r_id = r_id[r_id.find("id=")+3:]
                                detail = reli.find_all('li')
                                try:
                                    r_detail = detail[1].get_text()
                                except IndexError:
                                    pass
                        elif(section == "Political Views"):
                            pol = j.find(class_="uiList _4kg _6-h _704 _6-i")
                            if(isinstance(pol.find('a'), type(None))):
                                p_name = pol.get_text()
                            else:
                                p_name = pol.find('a').get_text()
                                p_id = pol.find('a')['data-hovercard']
                                p_id = p_id[p_id.find("id=")+3:]
                                detail = pol.find_all('li')
                                try:
                                    p_detail = detail[1].get_text()
                                except IndexError:
                                    pass
                        elif(section == "Languages"):
                            b_lan = True
                            for l in j.find_all(class_="_3l7z _39g6"):
                                lan_name = l.get_text()
                                lan_id = l['data-hovercard']
                                lan_id = lan_id[lan_id.find("id=")+3:]
                                w_lan.write(userID + " \"\" " + lan_name + " \"\" " + lan_id + "\n")

            if not(b_mob):
                w_mob.write(userID + " \"\" Empty\n")
            if not(address == "Empty"):
                for i,v in enumerate(address):
                    if(address[i:].isdigit()):
                        zipcode = address[i:]
                        address = address[:i]
                        break
            w_add.write(userID + " \"\" " + address + " \"\" " + zipcode + " \"\" " + neighborhood + "\n")
            if not(b_email):
                w_email.write(userID + " \"\" Empty\n")
            w_fb.write(userID + " \"\" " + fb + "\n")
            w_info.write(userID + " \"\" " + birth + " \"\" " + gender + " \"\" " + blood + " \"\" " + inter + " \"\" " + r_name + " \"\" " + r_id + " \"\" " + r_detail + " \"\" " + p_name + " \"\" " + p_id + " \"\" " + p_detail + "\n")
            if not(b_web):
                w_web.write(userID + " \"\" Empty\n")
            if not(b_link):
                w_link.write(userID + " \"\" Empty" + " \"\" Empty\n")
            if not(b_lan):
                w_lan.write(userID + " \"\" Empty" + " \"\" Empty\n")
        # Family and Relationships ######################################
        browser.find_element(By.XPATH, "//a[@class='_5pwr _Interaction__ProfileSectionAllRelationships']").click();
        time.sleep(random.randint(3,8)) ### Wait for 7 - 16 seconds
        soup = BeautifulSoup(browser.page_source,"html.parser")
        re_name = re_id = re_detail = "Empty"
        if not (isinstance(soup.find(class_="_4qm1"), type(None)) ): ### check to pass the user or not
            for i in soup.find_all(class_="_4qm1"):
                blockname = i.find('div').get_text() ### 2 blocks for Relationship / Family
                if (blockname=="Relationship"):
                    obj = i.find(class_="_2lzr _50f5 _50f7")
                    if not(isinstance(obj, type(None))):
                        re_name = obj.get_text()
                        re_id = obj.find('a')['data-hovercard']
                        re_id = re_id[re_id.find("id=")+3:]
                        re_detail = i.find(class_="_173e _50f8 _2ieq").get_text()
                    else:
                        detail = i.find(class_="_vb- _50f5")
                        if not(isinstance(detail, type(None))):
                            re_detail = detail.get_text()
                    w_rela.write(userID + " \"\" " + re_name + " \"\" " + re_id + " \"\" " + re_detail + "\n")
                else: # Family
                    fam_block = i.find(class_="_43c8 _2ge8")
                    if not(isinstance(fam_block, type(None))):
                        obj = i.find_all(class_="_42ef")
                        for j in obj:
                            fam_id = fam_detail = "Empty"
                            fam = j.find(class_="_2iel _50f7")
                            fam_name = fam.get_text()
                            if not(isinstance(fam.find('a'), type(None))):
                                fam_id = fam.find('a')['data-hovercard']
                                fam_id = fam_id[fam_id.find("id=")+3:]
                                detail = j.find_all(class_="fsm fwn fcg")
                                try:
                                    fam_detail = detail[1].get_text()
                                except IndexError:
                                    fam_detail = detail[0].get_text()
                            w_fam.write(userID + " \"\" " + fam_name + " \"\" " + fam_id + " \"\" " + fam_detail + "\n")
                    else:
                        w_fam.write(userID + " \"\" Empty" + " \"\" Empty" + " \"\" Empty\n")
        # Details About Him/Her ######################################
        browser.find_element(By.XPATH, "//*[@class='_5pwr _Interaction__ProfileSectionAbout']").click();
        time.sleep(random.randint(3,8)) ### Wait for 7 - 16 seconds
        soup = BeautifulSoup(browser.page_source,"html.parser")
        b_name = False
        about = quote = "Empty"
        if not (isinstance(soup.find(class_="_4qm1"), type(None)) ): ### check to pass the user or not
            for i in soup.find_all(class_="_4qm1"):
                blockname = i.find('div').get_text() ### 2 blocks for Other Names / About + Quotes
                if  (blockname=="Other Names"):
                    b_name = True
                    for n in i.find_all(class_="_43c8 _5f6p _3twh"):
                        o_name = n.find(class_="_2iem").get_text()
                        o_cate = n.find(class_="fsm fwn fcg").get_text()
                        w_other.write(userID + " \"\" " + o_name + " \"\" " + o_cate + "\n")
                else : ### About + Quotes
                    temp = i.find(class_="_c24 _50f4")
                    if not(isinstance(temp, type(None))):
                        if(blockname=="Favorite Quotes"):
                            quote = temp.get_text()
                        else:
                            about = temp.get_text()
        w_detail.write(userID + " \"\" " + about + " \"\" " + quote + "\n")
        if not(b_name):
            w_other.write(userID + " \"\" Empty" + " \"\" Empty\n")
        # Life Events ######################################
        browser.find_element(By.XPATH, "//*[@class='_5pwr _Interaction__ProfileSectionYearOverviews']").click();
        time.sleep(random.randint(3,8)) ### Wait for 7 - 16 seconds
        soup = BeautifulSoup(browser.page_source,"html.parser")
        cate = []
        detail = []
        href = []
        if not(isinstance(soup.find(class_="uiList _4kg _6-h _6-j _6-i"), type(None))):  ### check to pass the user or not
            for i in soup.find(class_="_4qm1").find_all(class_="uiList _4kg _6-h _6-j _6-i"):
                for j in i.find_all(class_="clearfix"): ### Find all events
                    c = str(j.find('i')) ### Fine the event category
                    if (c=="None"):
                        c = str(j.find('img'))
                        c = c[c.find("class=\"")+7:c.find("\" src")]
                    else:
                        c = c[c.find("class=\"")+7:c.find("\"></i>")]
                    cate.append(c)
                    d = j.find(class_="_c24 _2iem").get_text() ### Find the event detail
                    detail.append(str(d))
                    h = j.find(class_="_8u _42ef").find('a')['href'] ### Find the event href
                    href.append(str(h))
            for i,h in enumerate(href): ### Go to the event pages to get the people list, location
                h = h.replace('&amp;','&')
                browser.get("https://www.facebook.com"+href[i])
                time.sleep(random.randint(7,11))
                soup = BeautifulSoup(browser.page_source,"html.parser")
                p_time = soup.find(class_="_5pcp _5lel _2jyu _232_").find_all('div')[0].get('data-tooltip-content')
                p_time = str(p_time)
                if (p_time[0:8] == "Added on"):
                    p_time = p_time[9:]
                p_list = {}
                people = soup.find(class_="_7tae _14f3 _14f5 _5pbw _5vra").find_all('a')
                location = soup.find(class_="_7tae _14f3 _14f5 _5pbw _5vra").find('i')
                if not(isinstance(location, type(None))):
                    people = people[:-1]
                if(len(people) >= 2): #only poster
                    source = people[0].get('data-hovercard')
                    p_list[people[0].get_text()] = source[source.find('id=')+3:source.find('&')]
                    if(len(people)==3): #poster and 1 tag
                        source = people[2].get('data-hovercard')
                        p_list[people[2].get_text()] = source[source.find('id=')+3:source.find('&')]
                    elif(len(people)==4): #3 people or more
                        try:
                            browser.find_element_by_partial_link_text("others").click()
                            time.sleep(random.randint(7,11))
                            #browser.find_element_by_class_name('fbProfileBrowserListItem').click()
                            '''count = 0
                            while(count<10):
                                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                time.sleep(random.randint(5,10))
                                count += 1'''
                            p_soup= BeautifulSoup(browser.page_source,"html.parser")
                            for t in p_soup.find_all(class_="fbProfileBrowserListItem"):
                                name = t.find(class_="fsl fwb fcb").find('a').get_text()
                                ID = t.find(class_="fsl fwb fcb").find('a').get('data-gt')
                                ID = ID[ID.find("\"eng_tid\":")+11:ID.find("\",\"eng_data")]
                                print()
                                p_list[name] = ID
                        except NoSuchElementException:
                            source = people[3].get('data-hovercard')
                            p_list[people[3].get_text()] = source[source.find('id=')+3:source.find('&')]
                w_life.write(userID + " \"\" " + cate[i] + " \"\" " + p_time + " \"\" " + detail[i] + " \"\" " + str(p_list)+"\n")
        else:
            w_life.write(userID + " \"\" Empty" + " \"\" Empty" + " \"\" Empty" + " \"\" Empty\n")
    # Work & Education
    w_work.close()
    w_proskill.close()
    w_edu.close()
    # Places He/She's Lived
    w_CCH.close()     # CURRENT CITY AND HOMETOWN
    w_OPL.close()     # OTHER PLACES LIVED
    # Contact and Basic Info
    w_mob.close()
    w_add.close()
    w_email.close()
    w_fb.close()
    w_web.close()
    w_link.close()
    w_info.close()
    w_lan.close()
    # Family and Relationships
    w_rela.close()
    w_fam.close()
    # Details About Him/Her
    w_detail.close()
    w_other.close()
    # Life Events
    w_life.close()





def fb_About_edu(browser):
    print("\nAbout: Work & Education")
    w_work = codecs.open("data/data_work.txt",'w','utf-8-sig')
    w_proskill = codecs.open("data/data_proskill.txt",'w','utf-8-sig')
    w_edu = codecs.open("data/data_edu.txt",'w','utf-8-sig')
    for index, userID in enumerate(id_list):
        print(index, userID)
        userUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk=about&section=education"
        browser.get(userUrl)
        time.sleep(random.randint(7,16)) ### Wait for 7 - 16 seconds
        soup = BeautifulSoup(browser.page_source,"html.parser")
        b_work = b_edu = b_proskill = False
        if not (isinstance(soup.find(class_="_4qm1"), type(None)) ): ### check to pass the user or not
            for i in soup.find_all(class_="_4qm1"):
                blockname = i.find('div').get_text()  ### 2 block for Work + Edu / ProSkill
                if not(isinstance(i.find(class_="_43c8 _5f6p fbEditProfileViewExperience experience"), type(None) )):
                    if not(blockname=="Professional Skills"):
                        if(blockname=="Work"):
                            b_work = True
                            w = w_work
                        elif(blockname=="Education"):
                            b_edu = True
                            w = w_edu
                        else:
                            print("error occured")
                        for work in i.find_all(class_="_43c8 _5f6p fbEditProfileViewExperience experience"):
                            work_name = work.find(class_="_2lzr _50f5 _50f7")
                            work_ID = work_name.find('a')['data-hovercard']
                            w.write(userID + " \"\" " + work_name.get_text() + " \"\" " + work_ID[work_ID.find("id=")+3:])
                            work_b1 = work.find(class_="fsm fwn fcg")
                            if( isinstance(work_b1, type(None)) ):
                                w.write(" \"\" Empty")
                            else:
                                w.write(" \"\" " + work_b1.get_text())
                            if not(isinstance(work.find(class_="_5mqb"), type(None))):
                                work_b2 = work.find(class_="_5mqb")
                            else:
                                work_b2 = work.find(class_="_3-8w _50f8")
                            if( isinstance(work_b2, type(None)) ):
                                w.write(" \"\" Empty\n")
                            else:
                                w.write(" \"\" " + work_b2.get_text()+"\n")
                    else: ### ProSkill
                        b_proskill = True
                        for skill in i.find_all(class_="_3l7z _39g6"):
                            skill_name = skill.get_text()
                            skill_ID = skill['data-hovercard']
                            w_proskill.write(userID + " \"\" " + skill_name + " \"\" " + skill_ID[skill_ID.find("id=")+3:]+"\n")

            if not(b_work):
                w_work.write(userID + " \"\" Empty\n")
            if not(b_proskill):
                w_proskill.write(userID + " \"\" Empty\n")
            if not(b_edu):
                w_edu.write(userID + " \"\" Empty\n")

def fb_About_living(browser):
    print("\nAbout: Living Place")
    w_CCH = codecs.open("data/data_CCH.txt",'w','utf-8-sig')     # CURRENT CITY AND HOMETOWN
    w_OPL = codecs.open("data/data_OPL.txt",'w','utf-8-sig')     # OTHER PLACES LIVED
    for index, userID in enumerate(id_list):
        print(index, userID)
        userUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk=about&section=living"
        browser.get(userUrl)
        time.sleep(random.randint(7,11)) ### Wait for 5 - 10 seconds
        soup = BeautifulSoup(browser.page_source,"html.parser")
        b_OPL = False
        if not (isinstance(soup.find(class_="_4qm1"), type(None)) ): ### check to pass the user or not
            for i in soup.find_all(class_="_4qm1"):
                blockname = i.find('div').get_text() ### 2 bolcks for Current City + Hometown/Other Place Lived
                if (blockname=="Current City and Hometown"):
                    place = i.find_all(class_="_3pw9 _2pi4 _2ge8")
                    CC_name = CC_ID = HT_name = HT_ID = "Empty"
                    for j in place:
                        if( isinstance(j.find(class_="_2iel _50f7"), type(None)) ):
                            w_CCH.write(userID + " \"\" Empty" + " \"\" Empty" + " \"\" Empty" + " \"\" Empty\n")
                        else:
                            if(j.find(class_="fsm fwn fcg").get_text()=="Current city"):
                                CC = j.find(class_="_2iel _50f7")
                                CC_name = CC.get_text()
                                if not(isinstance(CC.find('a'), type(None))):
                                    CC_ID = CC.find('a')['data-hovercard']
                                CC_ID = CC_ID[CC_ID.find("id=")+3:]
                            elif(j.find(class_="fsm fwn fcg").get_text()=="Hometown"):
                                HT = j.find(class_="_2iel _50f7")
                                HT_name = HT.get_text()
                                if not(isinstance(HT.find('a'), type(None))):
                                    HT_ID = HT.find('a')['data-hovercard']
                                HT_ID = HT_ID[HT_ID.find("id=")+3:]
                    w_CCH.write(userID + " \"\" " + CC_name + " \"\" " + CC_ID + " \"\" " + HT_name + " \"\" " + HT_ID + "\n")
                else:
                    b_OPL = True
                    for place in i.find_all(class_="_43c8 _5f6p"):
                        place_name = place.find(class_="_2iel _50f7").get_text()
                        if not(isinstance(place.find(class_="_2iel _50f7").find('a'), type(None))):
                            place_ID = place.find(class_="_2iel _50f7").find('a')['data-hovercard']
                        else:
                            place_ID = "Empty"
                        place_detail = place.find(class_="fsm fwn fcg").get_text()
                        w_OPL.write(userID + " \"\" " + place_name + " \"\" " + place_ID[place_ID.find("id=")+3:] + " \"\" " + place_detail + "\n")
        if not(b_OPL):
            w_OPL.write(userID + " \"\" Empty" + " \"\" Empty" + " \"\" Empty\n")

def fb_About_info(browser):
    print("\nAbout: Contact & Basic Info")
    w_mob = codecs.open("data/data_mob.txt",'w','utf-8-sig')
    w_add = codecs.open("data/data_add.txt",'w','utf-8-sig')
    w_email = codecs.open("data/data_email.txt",'w','utf-8-sig')
    w_fb = codecs.open("data/data_fb.txt",'w','utf-8-sig')
    w_web = codecs.open("data/data_web.txt",'w','utf-8-sig')
    w_link = codecs.open("data/data_link.txt",'w','utf-8-sig')
    w_info = codecs.open("data/data_info.txt",'w','utf-8-sig')
    w_lan = codecs.open("data/data_lan.txt",'w','utf-8-sig')
    for index, userID in enumerate(id_list):
        print(index, userID)
        userUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk=about&section=contact-info"
        browser.get(userUrl)
        time.sleep(random.randint(7,11)) ### Wait for 5 - 10 seconds
        soup = BeautifulSoup(browser.page_source,"html.parser")
        b_mob = b_email = b_web = b_link = False
        address = zipcode = neighborhood = fb = "Empty"
        birth = gender = blood = inter = r_name = r_id = r_detail = p_name = p_id = p_detail = "Empty"
        b_lan = False
        if not (isinstance(soup.find(class_="_4qm1"), type(None)) ): ### check to pass the user or not
            for i in soup.find_all(class_="_4qm1"):
                blockname = i.find('div').get_text() ### 3 bolcks for Contact / Website / Information
                if (blockname=="Contact Information"):
                    for j in i.find_all(class_="clearfix _ikh"):
                        section = j.find(class_="_50f4 _5kx5").get_text()
                        if(section=="Mobile Phones"):
                            b_mob = True
                            phone = j.find_all("li")
                            for p in phone:
                                w_mob.write(userID + " \"\" " + p.get_text() + "\n")
                        elif(section=="Address"):
                            address = j.find(class_="_4bl7 _pt5").get_text()
                        elif(section=="Neighborhood"):
                            neighborhood = j.find(class_="_4bl7 _pt5").get_text()
                        elif(section=="Email"):
                            b_email = True
                            email = j.find_all(class_="_50f9 _50f7")
                            for e in email:
                                w_email.write(userID + " \"\" " + e.get_text() + "\n")
                        else: #FB
                            fb = j.find(class_="_4bl7 _pt5").get_text()
                elif(blockname=="Websites and Social Links"):
                    for j in i.find_all(class_="clearfix _ikh"):
                        section = j.find(class_="_50f4 _5kx5").get_text()
                        if(section=="Websites"):
                            b_web = True
                            for web in j.find_all(class_="_39g6"):
                                w_web.write(userID + " \"\" " + web.get_text() + "\n")
                        else: #social link
                            b_link = True
                            for link in j.find_all(class_="uiList _509- _4ki _6-h _6-j _6-i"):
                                social_link = link.find_all('li')[0].get_text()
                                cate = link.find_all('li')[1].get_text()
                                w_link.write(userID + " \"\" " + social_link + " \"\" " + cate + "\n")
                else: # Basic Information
                    for j in i.find_all(class_="clearfix _ikh"):
                        section = j.find(class_="_50f4 _5kx5").get_text()
                        temp = j.find(class_="_4bl7 _pt5").get_text()
                        if(section == "Birthday"):
                            if not(temp[:8]=="Ask for "):
                                birth = temp
                        elif(section == "Gender"):
                            gender = temp
                        elif(section == "Blood Type"):
                            blood = temp
                        elif(section == "Interested In"):
                            inter = temp
                        elif(section == "Religious Views"):
                            reli = j.find(class_="uiList _4kg _6-h _704 _6-i")
                            if(isinstance(reli.find('a'), type(None))):
                                r_name = reli.get_text()
                            else:
                                r_name = reli.find('a').get_text()
                                r_id = reli.find('a')['data-hovercard']
                                r_id = r_id[r_id.find("id=")+3:]
                                detail = reli.find_all('li')
                                try:
                                    r_detail = detail[1].get_text()
                                except IndexError:
                                    pass
                        elif(section == "Political Views"):
                            pol = j.find(class_="uiList _4kg _6-h _704 _6-i")
                            if(isinstance(pol.find('a'), type(None))):
                                p_name = pol.get_text()
                            else:
                                p_name = pol.find('a').get_text()
                                p_id = pol.find('a')['data-hovercard']
                                p_id = p_id[p_id.find("id=")+3:]
                                detail = pol.find_all('li')
                                try:
                                    p_detail = detail[1].get_text()
                                except IndexError:
                                    pass
                        elif(section == "Languages"):
                            b_lan = True
                            for l in j.find_all(class_="_3l7z _39g6"):
                                lan_name = l.get_text()
                                lan_id = l['data-hovercard']
                                lan_id = lan_id[lan_id.find("id=")+3:]
                                w_lan.write(userID + " \"\" " + lan_name + " \"\" " + lan_id + "\n")

            if not(b_mob):
                w_mob.write(userID + " \"\" Empty\n")
            if not(address == "Empty"):
                for i,v in enumerate(address):
                    if(address[i:].isdigit()):
                        zipcode = address[i:]
                        address = address[:i]
                        break
            w_add.write(userID + " \"\" " + address + " \"\" " + zipcode + " \"\" " + neighborhood + "\n")
            if not(b_email):
                w_email.write(userID + " \"\" Empty\n")
            w_fb.write(userID + " \"\" " + fb + "\n")
            w_info.write(userID + " \"\" " + birth + " \"\" " + gender + " \"\" " + blood + " \"\" " + inter + " \"\" " + r_name + " \"\" " + r_id + " \"\" " + r_detail + " \"\" " + p_name + " \"\" " + p_id + " \"\" " + p_detail + "\n")
            if not(b_web):
                w_web.write(userID + " \"\" Empty\n")
            if not(b_link):
                w_link.write(userID + " \"\" Empty" + " \"\" Empty\n")
            if not(b_lan):
                w_lan.write(userID + " \"\" Empty" + " \"\" Empty\n")

def fb_About_rela(browser):
    print("\nAbout: Family & Relationships")
    w_rela = codecs.open("data/data_rela.txt",'w','utf-8-sig')
    w_fam = codecs.open("data/data_fam.txt",'w','utf-8-sig')
    for index, userID in enumerate(id_list):
        print(index, userID)
        userUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk=about&section=relationship"
        browser.get(userUrl)
        time.sleep(random.randint(7,11)) ### Wait for 5 - 10 seconds
        soup = BeautifulSoup(browser.page_source,"html.parser")
        re_name = re_id = re_detail = "Empty"
        if not (isinstance(soup.find(class_="_4qm1"), type(None)) ): ### check to pass the user or not
            for i in soup.find_all(class_="_4qm1"):
                blockname = i.find('div').get_text() ### 2 blocks for Relationship / Family
                if (blockname=="Relationship"):
                    obj = i.find(class_="_2lzr _50f5 _50f7")
                    if not(isinstance(obj, type(None))):
                        re_name = obj.get_text()
                        re_id = obj.find('a')['data-hovercard']
                        re_id = re_id[re_id.find("id=")+3:]
                        re_detail = i.find(class_="_173e _50f8 _2ieq").get_text()
                    else:
                        detail = i.find(class_="_vb- _50f5")
                        if not(isinstance(detail, type(None))):
                            re_detail = detail.get_text()
                    w_rela.write(userID + " \"\" " + re_name + " \"\" " + re_id + " \"\" " + re_detail + "\n")
                else: # Family
                    fam_block = i.find(class_="_43c8 _2ge8")
                    if not(isinstance(fam_block, type(None))):
                        obj = i.find_all(class_="_42ef")
                        for j in obj:
                            fam_id = fam_detail = "Empty"
                            fam = j.find(class_="_2iel _50f7")
                            fam_name = fam.get_text()
                            if not(isinstance(fam.find('a'), type(None))):
                                fam_id = fam.find('a')['data-hovercard']
                                fam_id = fam_id[fam_id.find("id=")+3:]
                                detail = j.find_all(class_="fsm fwn fcg")
                                try:
                                    fam_detail = detail[1].get_text()
                                except IndexError:
                                    fam_detail = detail[0].get_text()
                            w_fam.write(userID + " \"\" " + fam_name + " \"\" " + fam_id + " \"\" " + fam_detail + "\n")
                    else:
                        w_fam.write(userID + " \"\" Empty" + " \"\" Empty" + " \"\" Empty\n")

def fb_About_bio(browser):
    print("\nAbout: Details")
    w_detail = codecs.open("data/data_detail.txt",'w','utf-8-sig')
    w_other = codecs.open("data/data_other.txt",'w','utf-8-sig')
    for index, userID in enumerate(id_list):
        print(index, userID)
        userUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk=about&section=bio"
        browser.get(userUrl)
        time.sleep(random.randint(7,11)) ### Wait for 5 - 10 seconds
        soup = BeautifulSoup(browser.page_source,"html.parser")
        b_name = False
        about = quote = "Empty"
        if not (isinstance(soup.find(class_="_4qm1"), type(None)) ): ### check to pass the user or not
            for i in soup.find_all(class_="_4qm1"):
                blockname = i.find('div').get_text() ### 2 blocks for Other Names / About + Quotes
                if  (blockname=="Other Names"):
                    b_name = True
                    for n in i.find_all(class_="_43c8 _5f6p _3twh"):
                        o_name = n.find(class_="_2iem").get_text()
                        o_cate = n.find(class_="fsm fwn fcg").get_text()
                        w_other.write(userID + " \"\" " + o_name + " \"\" " + o_cate + "\n")
                else : ### About + Quotes
                    temp = i.find(class_="_c24 _50f4")
                    if not(isinstance(temp, type(None))):
                        if(blockname=="Favorite Quotes"):
                            quote = temp.get_text()
                        else:
                            about = temp.get_text()
        w_detail.write(userID + " \"\" " + about + " \"\" " + quote + "\n")
        if not(b_name):
            w_other.write(userID + " \"\" Empty" + " \"\" Empty\n")

def fb_About_life(browser):
    print("\nAbout: Life Events")
    w_life = codecs.open("data/data_life.txt",'w','utf-8-sig')
    for index, userID in enumerate(id_list):
        print(index, userID)
        userUrl = "https://www.facebook.com/profile.php?id="+userID+"&sk=about&section=year-overviews"
        browser.get(userUrl)
        time.sleep(random.randint(7,11))
        soup = BeautifulSoup(browser.page_source,"html.parser")
        cate = []
        detail = []
        href = []
        if not(isinstance(soup.find(class_="uiList _4kg _6-h _6-j _6-i"), type(None))):  ### check to pass the user or not
            for i in soup.find(class_="_4qm1").find_all(class_="uiList _4kg _6-h _6-j _6-i"):
                for j in i.find_all(class_="clearfix"): ### Find all events
                    c = str(j.find('i')) ### Fine the event category
                    if (c=="None"):
                        c = str(j.find('img'))
                        c = c[c.find("class=\"")+7:c.find("\" src")]
                    else:
                        c = c[c.find("class=\"")+7:c.find("\"></i>")]
                    cate.append(c)
                    d = j.find(class_="_c24 _2iem").get_text() ### Find the event detail
                    detail.append(str(d))
                    h = j.find(class_="_8u _42ef").find('a')['href'] ### Find the event href
                    href.append(str(h))
            for i,h in enumerate(href): ### Go to the event pages to get the people list, location
                h = h.replace('&amp;','&')
                browser.get("https://www.facebook.com"+href[i])
                time.sleep(random.randint(7,11))
                soup = BeautifulSoup(browser.page_source,"html.parser")
                p_time = soup.find(class_="_5pcp _5lel _2jyu _232_").find_all('div')[0].get('data-tooltip-content')
                p_time = str(p_time)
                if (p_time[0:8] == "Added on"):
                    p_time = p_time[9:]
                p_list = {}
                people = soup.find(class_="_14f3 _14f5 _5pbw _5vra").find_all('a')
                location = soup.find(class_="_14f3 _14f5 _5pbw _5vra").find('i')
                if not(isinstance(location, type(None))):
                    people = people[:-1]
                if(len(people) >= 2): #only poster
                    source = people[0].get('data-hovercard')
                    p_list[people[0].get_text()] = source[source.find('id=')+3:source.find('&')]
                    if(len(people)==3): #poster and 1 tag
                        source = people[2].get('data-hovercard')
                        p_list[people[2].get_text()] = source[source.find('id=')+3:source.find('&')]
                    elif(len(people)==4): #3 people or more
                        try:
                            browser.find_element_by_partial_link_text("others").click()
                            time.sleep(random.randint(7,11))
                            #browser.find_element_by_class_name('fbProfileBrowserListItem').click()
                            '''count = 0
                            while(count<10):
                                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                time.sleep(random.randint(5,10))
                                count += 1'''
                            p_soup= BeautifulSoup(browser.page_source,"html.parser")
                            for t in p_soup.find_all(class_="fbProfileBrowserListItem"):
                                name = t.find(class_="fsl fwb fcb").find('a').get_text()
                                ID = t.find(class_="fsl fwb fcb").find('a').get('data-gt')
                                ID = ID[ID.find("\"eng_tid\":")+11:ID.find("\",\"eng_data")]
                                print()
                                p_list[name] = ID
                        except NoSuchElementException:
                            source = people[3].get('data-hovercard')
                            p_list[people[3].get_text()] = source[source.find('id=')+3:source.find('&')]
                w_life.write(userID + " \"\" " + cate[i] + " \"\" " + p_time + " \"\" " + detail[i] + " \"\" " + str(p_list)+"\n")
        else:
            w_life.write(userID + " \"\" Empty" + " \"\" Empty" + " \"\" Empty" + " \"\" Empty\n")
