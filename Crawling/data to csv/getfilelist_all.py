import csv

# 開啟輸出的 CSV 檔案
with open('../output_all.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    # 寫入標題
    W1 = ['work_1', 'work_2', 'work_3', 'work_4', 'proskill_1', 'edu_1', 'edu_2', 'edu_3', 'edu_4']
    W2 = ['cch_1', 'cch_2', 'cch_3', 'cch_4', 'opl_1', 'opl_2', 'opl_3']
    W3 = ['mob_1', 'add_1', 'add_2', 'add_3', 'email_1']
    W4 = ['fb_1', 'web_1', 'link_1', 'link_2']
    W5 = ['Birthday', 'Gender', 'Blood Type', 'Interested In', 'Religious Views_1', 'Religious Views_2', 'Religious Views_3', 'Political Views_1', 'Political Views_2', 'Political Views_3', 'Languages_1', 'Languages_2']
    W6 = ['rela_1', 'rela_2', 'rela_3', 'fam_1', 'fam_2', 'fam_3']
    W7 = ['detail_1', 'detail_2', 'other_1', 'other_2']
    W8 = ['life_1', 'life_2', 'life_3', 'life_4']
    W9 = ['friend count']
    W10 = ['post_amount_10', 'post_shared_10', 'post_frequency_10', 'post_amount_20', 'post_shared_20', 'post_frequency_20', 'post_year_count', 'LABEL']
    
    
    writer.writerow(['ID']+W1+W2+W3+W4+W5+W6+W7+W8+W9+W10)
    # 讀檔
    p_add = open("../data_positive/data_add.txt",'r', encoding = 'utf8')
    p_cch = open("../data_positive/data_cch.txt",'r', encoding = 'utf8')
    p_detail = open("../data_positive/data_detail.txt",'r', encoding = 'utf8')
    p_email = open("../data_positive/data_email.txt",'r', encoding = 'utf8')
    p_fb = open("../data_positive/data_fb.txt",'r', encoding = 'utf8')
    p_mob = open("../data_positive/data_mob.txt",'r', encoding = 'utf8')
    p_proskill = open("../data_positive/data_proskill.txt",'r', encoding = 'utf8')
    p_rela = open("../data_positive/data_rela.txt",'r', encoding = 'utf8')
    
    p_edu = open("../data_positive/data_edu.txt",'r', encoding = 'utf8')
    p_fam = open("../data_positive/data_fam.txt",'r', encoding = 'utf8')
    p_info = open("../data_positive/data_info.txt",'r', encoding = 'utf8')
    p_lan = open("../data_positive/data_lan.txt",'r', encoding = 'utf8')
    p_life = open("../data_positive/data_life.txt",'r', encoding = 'utf8')
    p_link = open("../data_positive/data_link.txt",'r', encoding = 'utf8')
    p_opl = open("../data_positive/data_OPL.txt",'r', encoding = 'utf8')
    p_other = open("../data_positive/data_other.txt",'r', encoding = 'utf8')
    p_web = open("../data_positive/data_web.txt",'r', encoding = 'utf8')
    p_work = open("../data_positive/data_work.txt",'r', encoding = 'utf8')
    
    p_friend = open("../data_positive/data_friendsCNT.txt",'r', encoding = 'utf8')
    p_post = open("../data_positive/data_post.txt",'r', encoding = 'utf8')
    # 分行
    p_Add = p_add.read().splitlines()
    p_Cch = p_cch.read().splitlines()
    p_Detail = p_detail.read().splitlines()
    p_Email = p_email.read().splitlines()
    p_Fb = p_fb.read().splitlines()
    p_Mob = p_mob.read().splitlines()
    p_Proskill = p_proskill.read().splitlines()
    p_Rela = p_rela.read().splitlines()
    
    p_Edu = p_edu.read().splitlines()
    p_Fam = p_fam.read().splitlines()
    p_Info = p_info.read().splitlines()
    p_Lan = p_lan.read().splitlines()
    p_Life = p_life.read().splitlines()
    p_Link = p_link.read().splitlines()
    p_Opl = p_opl.read().splitlines()
    p_Other = p_other.read().splitlines()
    p_Web = p_web.read().splitlines()
    p_Work = p_work.read().splitlines()
    
    p_Friend = p_friend.read().splitlines()
    p_Post = p_post.read().splitlines()
    #decode
    p_Add[0]= p_Add[0].encode('utf-8').decode('utf-8-sig')
    p_Cch[0]= p_Cch[0].encode('utf-8').decode('utf-8-sig')
    p_Detail[0]= p_Detail[0].encode('utf-8').decode('utf-8-sig')
    p_Email[0]= p_Email[0].encode('utf-8').decode('utf-8-sig')
    p_Fb[0]= p_Fb[0].encode('utf-8').decode('utf-8-sig')
    p_Mob[0]= p_Mob[0].encode('utf-8').decode('utf-8-sig')
    p_Proskill[0]= p_Proskill[0].encode('utf-8').decode('utf-8-sig')
    p_Rela[0]= p_Rela[0].encode('utf-8').decode('utf-8-sig')
    
    p_Edu[0]= p_Edu[0].encode('utf-8').decode('utf-8-sig')
    p_Fam[0]= p_Fam[0].encode('utf-8').decode('utf-8-sig')
    p_Info[0]= p_Info[0].encode('utf-8').decode('utf-8-sig')
    p_Lan[0]= p_Lan[0].encode('utf-8').decode('utf-8-sig')
    p_Life[0]= p_Life[0].encode('utf-8').decode('utf-8-sig')
    p_Link[0]= p_Link[0].encode('utf-8').decode('utf-8-sig')
    p_Opl[0]= p_Opl[0].encode('utf-8').decode('utf-8-sig')
    p_Other[0]= p_Other[0].encode('utf-8').decode('utf-8-sig')
    p_Web[0]= p_Web[0].encode('utf-8').decode('utf-8-sig')
    p_Work[0]= p_Work[0].encode('utf-8').decode('utf-8-sig')
    p_Friend[0]= p_Friend[0].encode('utf-8').decode('utf-8-sig')
    p_Post[0]= p_Post[0].encode('utf-8').decode('utf-8-sig')
    # 處理原檔    
    for p in [p_Add, p_Cch, p_Detail, p_Email, p_Fb, p_Mob, p_Proskill, p_Rela, p_Fam, p_Info, p_Lan, p_Life, p_Link, p_Opl, p_Other, p_Web, p_Friend, p_Post]:
        for i in range(len(p)):
            p[i] = p[i].encode("cp950", "replace").decode("cp950")
            p[i] = p[i].split(' "" ')
    print(p_Friend[0])
    for p in [p_Edu, p_Work]:
        for i in range(len(p)):
            p[i] = p[i].encode("cp950", "replace").decode("cp950")
            p[i] = p[i].split(' "" ')
            if p[i][1] == 'Empty':
                p[i].append('Empty')
                p[i].append('Empty')
                p[i].append('Empty')
    for p in [p_Friend, p_Post]:
        for i in range(len(p)):
            p[i][0] = p[i][0].replace('?', '')
    #for i in range
    # 寫入另外幾列資料
    c1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    c2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
# =============================================================================
# p_Edu, p_Work
# p_Add, p_Cch, p_Detail, p_Email, p_Fb, p_Mob, p_Proskill, p_Rela
# p_Fam, p_Info, p_Lan, p_Life, p_Link, p_Opl, p_Other, p_Web
# p_Friend, p_Post
# =============================================================================


    L1 = [p_Work, p_Proskill, p_Edu]
    L2 = [p_Cch, p_Opl]
    L3 = [p_Mob, p_Add, p_Email]
    L4 = [p_Fb, p_Web, p_Link]
    L5 = [p_Info, p_Lan]
    
    L6 = [p_Rela, p_Fam]
    L7 = [p_Detail, p_Other]
    L8 = [p_Life]
    
    L9 = [p_Friend]
    L10 = [p_Post]
    for i in range(len(p_Add)):
        #print(i)
        row_i = [p_Add[i][0]]
        for idx, p in enumerate(L1+L2+L3+L4+L5+L6+L7+L8+L9+L10):
            while c2[idx] < len(p) and p[c2[idx]][0] == p_Add[i][0]:
                c2[idx] = c2[idx]+1
            for j in range(1, len(p[c1[idx]])):
                list_j = []
                for k in range(c1[idx], c2[idx]):
                    list_j.append(p[k][j])
                row_i = row_i + [list_j]
            c1[idx] = c2[idx]
# =============================================================================
#         positive label
# =============================================================================
        row_i = row_i + [1]
        writer.writerow(row_i)
        
    p_add.close()
    p_edu.close()
    p_fam.close()
    p_info.close()
    p_lan.close()
    p_life.close()
    p_link.close()
    p_opl.close()
    p_other.close()
    p_web.close()
    p_work.close()
    p_friend.close()
    p_post.close()

##############################################################################
##############################################################################
##############################################################################

    # 讀檔
    p_add = open("../data_negative/data_add.txt",'r', encoding = 'utf8')
    p_cch = open("../data_negative/data_cch.txt",'r', encoding = 'utf8')
    p_detail = open("../data_negative/data_detail.txt",'r', encoding = 'utf8')
    p_email = open("../data_negative/data_email.txt",'r', encoding = 'utf8')
    p_fb = open("../data_negative/data_fb.txt",'r', encoding = 'utf8')
    p_mob = open("../data_negative/data_mob.txt",'r', encoding = 'utf8')
    p_proskill = open("../data_negative/data_proskill.txt",'r', encoding = 'utf8')
    p_rela = open("../data_negative/data_rela.txt",'r', encoding = 'utf8')
    
    p_edu = open("../data_negative/data_edu.txt",'r', encoding = 'utf8')
    p_fam = open("../data_negative/data_fam.txt",'r', encoding = 'utf8')
    p_info = open("../data_negative/data_info.txt",'r', encoding = 'utf8')
    p_lan = open("../data_negative/data_lan.txt",'r', encoding = 'utf8')
    p_life = open("../data_negative/data_life.txt",'r', encoding = 'utf8')
    p_link = open("../data_negative/data_link.txt",'r', encoding = 'utf8')
    p_opl = open("../data_negative/data_OPL.txt",'r', encoding = 'utf8')
    p_other = open("../data_negative/data_other.txt",'r', encoding = 'utf8')
    p_web = open("../data_negative/data_web.txt",'r', encoding = 'utf8')
    p_work = open("../data_negative/data_work.txt",'r', encoding = 'utf8')
    
    p_friend = open("../data_negative/data_friendsCNT.txt",'r', encoding = 'utf8')
    p_post = open("../data_negative/data_post.txt",'r', encoding = 'utf8')
    # 分行
    p_Add = p_add.read().splitlines()
    p_Cch = p_cch.read().splitlines()
    p_Detail = p_detail.read().splitlines()
    p_Email = p_email.read().splitlines()
    p_Fb = p_fb.read().splitlines()
    p_Mob = p_mob.read().splitlines()
    p_Proskill = p_proskill.read().splitlines()
    p_Rela = p_rela.read().splitlines()
    
    p_Edu = p_edu.read().splitlines()
    p_Fam = p_fam.read().splitlines()
    p_Info = p_info.read().splitlines()
    p_Lan = p_lan.read().splitlines()
    p_Life = p_life.read().splitlines()
    p_Link = p_link.read().splitlines()
    p_Opl = p_opl.read().splitlines()
    p_Other = p_other.read().splitlines()
    p_Web = p_web.read().splitlines()
    p_Work = p_work.read().splitlines()
    
    p_Friend = p_friend.read().splitlines()
    p_Post = p_post.read().splitlines()
    #decode
    p_Add[0]= p_Add[0].encode('utf-8').decode('utf-8-sig')
    p_Cch[0]= p_Cch[0].encode('utf-8').decode('utf-8-sig')
    p_Detail[0]= p_Detail[0].encode('utf-8').decode('utf-8-sig')
    p_Email[0]= p_Email[0].encode('utf-8').decode('utf-8-sig')
    p_Fb[0]= p_Fb[0].encode('utf-8').decode('utf-8-sig')
    p_Mob[0]= p_Mob[0].encode('utf-8').decode('utf-8-sig')
    p_Proskill[0]= p_Proskill[0].encode('utf-8').decode('utf-8-sig')
    p_Rela[0]= p_Rela[0].encode('utf-8').decode('utf-8-sig')
    
    p_Edu[0]= p_Edu[0].encode('utf-8').decode('utf-8-sig')
    p_Fam[0]= p_Fam[0].encode('utf-8').decode('utf-8-sig')
    p_Info[0]= p_Info[0].encode('utf-8').decode('utf-8-sig')
    p_Lan[0]= p_Lan[0].encode('utf-8').decode('utf-8-sig')
    p_Life[0]= p_Life[0].encode('utf-8').decode('utf-8-sig')
    p_Link[0]= p_Link[0].encode('utf-8').decode('utf-8-sig')
    p_Opl[0]= p_Opl[0].encode('utf-8').decode('utf-8-sig')
    p_Other[0]= p_Other[0].encode('utf-8').decode('utf-8-sig')
    p_Web[0]= p_Web[0].encode('utf-8').decode('utf-8-sig')
    p_Work[0]= p_Work[0].encode('utf-8').decode('utf-8-sig')
    
    p_Friend[0]= p_Friend[0].encode('utf-8').decode('utf-8-sig')
    p_Post[0]= p_Post[0].encode('utf-8').decode('utf-8-sig')
    # 處理原檔
    for p in [p_Add, p_Cch, p_Detail, p_Email, p_Fb, p_Mob, p_Proskill, p_Rela, p_Fam, p_Info, p_Lan, p_Life, p_Link, p_Opl, p_Other, p_Web, p_Friend, p_Post]:
        for i in range(len(p)):
            p[i] = p[i].encode("cp950", "replace").decode("cp950")
            p[i] = p[i].split(' "" ')
            #print(p[i])
    for p in [p_Edu, p_Work]:
        for i in range(len(p)):
            p[i] = p[i].encode("cp950", "replace").decode("cp950")
            p[i] = p[i].split(' "" ')
            if p[i][1] == 'Empty':
                p[i].append('Empty')
                p[i].append('Empty')
                p[i].append('Empty')
    for p in [p_Friend, p_Post]:
        for i in range(len(p)):
            p[i][0] = p[i][0].replace('?', '')
    #for i in range
    # 寫入另外幾列資料
    c1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    c2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
# =============================================================================
# p_Edu, p_Work
# p_Add, p_Cch, p_Detail, p_Email, p_Fb, p_Mob, p_Proskill, p_Rela
# p_Fam, p_Info, p_Lan, p_Life, p_Link, p_Opl, p_Other, p_Web
# p_Friend, p_Post
# =============================================================================


    L1 = [p_Work, p_Proskill, p_Edu]
    L2 = [p_Cch, p_Opl]
    L3 = [p_Mob, p_Add, p_Email]
    L4 = [p_Fb, p_Web, p_Link]
    L5 = [p_Info, p_Lan]
    L6 = [p_Rela, p_Fam]
    L7 = [p_Detail, p_Other]
    L8 = [p_Life]
    
    L9 = [p_Friend]
    L10 = [p_Post]
    for i in range(len(p_Add)):
        #print(i)
        row_i = [p_Add[i][0]]
        for idx, p in enumerate(L1+L2+L3+L4+L5+L6+L7+L8+L9+L10):
            while c2[idx] < len(p) and p[c2[idx]][0] == p_Add[i][0]:
                c2[idx] = c2[idx]+1
            for j in range(1, len(p[c1[idx]])):
                list_j = []
                for k in range(c1[idx], c2[idx]):
                    list_j.append(p[k][j])
                row_i = row_i + [list_j]
            c1[idx] = c2[idx]
# =============================================================================
#         positive label
# =============================================================================
        row_i = row_i + [0]
        writer.writerow(row_i)

    p_add.close()
    p_edu.close()
    p_fam.close()
    p_info.close()
    p_lan.close()
    p_life.close()
    p_link.close()
    p_opl.close()
    p_other.close()
    p_web.close()
    p_work.close()
    p_friend.close()
    p_post.close()