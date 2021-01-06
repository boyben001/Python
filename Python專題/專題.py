# 中英歌單，歌詞，回答用數字編排，男女歌手
# 歌曲類型:抒情，搖滾，R&B，嘻哈
# 用中文或英文來問與答
import time
import os
list_1 = []  # 歌曲評價收藏專用
list_2 = []  # 歌曲評價收藏專用
list_3 = []  # 歌曲評價收藏專用
list_4 = []  # 歌曲評價收藏專用
list_5 = []  # 歌曲評價收藏專用
chinese_dic = {"想見你想見你想見你": "抒情", "你好不好": "抒情", "我很快樂": "抒情", "地球上最浪漫的一首歌": "抒情", "刻在我心底的名字": "抒情", "我不是饒舌歌手": "搖滾", "重感情的廢物": "搖滾", "23": "搖滾", "擋一根": "搖滾", "捲菸": "搖滾",
               "七十億分之一加一": "R&B", "闖空門": "R&B", "所謂的愛": "R&B", "別問很可怕": "R&B", "慣性取暖": "R&B", "local": "嘻哈", "without you": "嘻哈", "colorful": "嘻哈", "伯父": "嘻哈", "走跳": "嘻哈"}
En_Dic = {'Classical': {'Opera': ['Tosca', 'Pagliacci', 'Luisa Miller', 'Turandot',
                                  'Carmen'],
                        'Instrumental': ['Four Seasons', 'Canon',
                                         'Moonlight Sonata', 'Winter Wind']},
          'PoP': {'Taylor Swift': ['Style', '22', 'You Belong With Me'],
                  'Selina Gomez': ['Lose You To Love Me', 'Wolves', 'Past Life'],
                  'Katy Perry': ['Roar', 'Last Friday Night', 'Part of Me'],
                  'Charlie Puth': ['Attention', 'How Long', 'One Call Away'],
                  'Shawn Mendes': ['Stitches', 'Treat You Better', 'In My Blood']}}


def AddEnSong(Song):  # 增加新歌曲到英文資料庫
    while True:  # 輸入錯誤，重新輸入
        print("We will ask you a few questions about " + Song + ".")
        print("Is " + Song + " Classical or PoP?\n")  # 歌的類型
        CP = str(input("Ans: "))  # 輸入歌曲類型
        if CP == 'Classical':
            print("Is " + Song + " Opera or Instrumental?\n")  # 歌的類型
            OI = str(input("Ans: "))  # 輸入歌曲類型
            En_Dic[CP][OI].append(Song)  # 增加Song
        elif CP == 'PoP':
            print("Who is the artist of " + Song +
                  "?(Input Space_Bar if Unknown)\n")  # 作者
            Singers = list(En_Dic['PoP'].keys())  # 目前歌手
            Singer = str(input("Ans: "))
            if Singer == ' ':  # 空格統一當作Unknown
                Singer = 'Unknown'
            if Singer in Singers:  # 已存在
                En_Dic[CP][Singer].append(Song)
            else:  # 新建PoP歌手的歌list
                En_Dic[CP][Singer] = [Song]
        else:
            print("Input Incorrect, Please retry.\n")
            continue  # 回到while
        break


def English():  # 選擇英文歌
    while True:  # 輸入錯誤，重新輸入
        print("Would you like to hear Classical or PoP?(Classical/PoP)\n")
        Search = str(input("Ans: "))
        print("\n")
        if Search == 'Classical':
            Classical()  # 跳到Classical()
        elif Search == 'PoP':
            PoP()  # 跳到PoP()
        else:
            print("Input Incorrect, Please retry.\n")
            continue
        break


def Classical():
    while True:  # 輸入錯誤，重新輸入
        print("Would you like to hear Opera or Instrumental?(Opera/Instrumental)\n")
        Search = str(input("Ans: "))
        print("\n")
        if Search == 'Opera':
            while True:  # 輸入錯誤，重新輸入
                for rand in En_Dic['Classical']['Opera']:  # 列出歌曲
                    print(rand)
                print("Choose a song: \n")
                Song = str(input("Ans: "))  # 輸入歌曲名
                print("\n")
                if Song == ' ':
                    print("Wrong Input! 'Space_Bar' cannot be independent!\n")
                    continue
                if Song in En_Dic['Classical']['Opera']:
                    # lyric(Song)  # 跳到dev lyric(name)
                    evaluation(Song)  # 跳到dev evaluation(abc)
                    break
                else:
                    print("Not Found!\n")
                    AddEnSong(Song)  # 跳到AddEnSong(Song)
        elif Search == 'Instrumental':
            while True:  # 輸入錯誤，重新輸入
                for rand in En_Dic['Classical']['Instrumental']:
                    print(rand)
                print("Choose a song: \n")
                Song = str(input("Ans: "))  # 輸入歌曲名
                print("\n")
                if Song == ' ':
                    print("Wrong Input! 'Space_Bar' cannot be independent!\n")
                    continue
                if Song in En_Dic['Classical']['Instrumental']:
                    evaluation(Song)  # 跳到dev evaluation(abc)
                    break
                else:
                    print("Not Found!\n")
                    AddEnSong(Song)  # 跳到AddEnSong(Song)

        else:
            print("Input Incorrect, Please retry.\n")
            continue
        break


def PoP():
    while True:  # 歌手+歌不存在 建立後 回到這裡繼續輸入
        print("Which musician's song would you like to hear?\n")
        Singers = list(En_Dic['PoP'].keys())
        print(Singers)
        Musician = str(input("Ans: "))  # 輸入歌手名
        print("\n")
        if Musician == ' ':
            Musician = 'Unknown'
        if Musician in Singers:
            while True:  # 歌不存在 建立後 回到這裡繼續輸入
                for rand in En_Dic['PoP'][Musician]:
                    print(rand)
                print("Which Song Would You Like To Hear?\n")
                Song = str(input("Ans: "))  # 輸入歌曲名
                if Song == ' ':
                    print("Wrong Input! 'Space_Bar' cannot be independent!\n")
                    continue
                if Song in En_Dic['PoP'][Musician]:
                    lyric(Song)  # 跳到dev lyric(name)
                    evaluation(Song)  # 跳到dev evaluation(abc)
                    break
                else:
                    print("Not Found!\n")
                    AddEnSong(Song)  # 跳到AddEnSong(Song)
            break
        else:
            print("Not Found!\n")
            while True:  # 輸入錯誤，重新輸入
                print("What Song would you like to hear?\n")
                Song = str(input("Ans: "))
                print("\n")
                if Song == ' ':
                    print("Wrong Input! 'Space_Bar' cannot be independent!\n")
                    continue
                else:
                    break
            AddEnSong(Song)  # 跳到AddEnSong(Song)


def rank_list(stars, abc):
    if (stars == 1):
        list_1.append(abc)
    elif (stars == 2):
        list_2.append(abc)
    elif (stars == 3):
        list_3.append(abc)
    elif (stars == 4):
        list_4.append(abc)
    elif (stars == 5):
        list_5.append(abc)


def kind(name):  # 歌曲添加
    print('\n')
    print("目前歌庫內沒有這首歌哦 !   !   ! ")
    print("請問要添加歌曲到歌庫內嗎? (是 / 否) : ", end='')
    while True:
        ans = str(input())
        if (ans == '是'):
            print("\n. . . 請輸入''細節''有關想添加的歌曲 . . .\n")
            print("請輸入歌曲種類 (抒情 /搖滾 /R&B /嘻哈): ", end='')
            while True:
                sort = str(input())
                if (sort == '抒情' or sort == '搖滾' or sort == 'r&b' or sort == 'R&B' or sort == '嘻哈'):
                    chinese_dic[name] = sort  # 添加歌曲到chinese_dic
                    time.sleep(0.5)
                    print("成功加入清單內 ! 　! 　! ")
                    time.sleep(0.5)
                    os.system("cls")
                    chinese()
                else:
                    print("輸入不對哦 ~ ~ ~　\n重新輸入: ", end='')
        elif (ans == '否'):
            print("結束歌曲添加功能　！　！　！")
            print("即將返回歌曲搜尋功能　~ ~ ~ ")
            time.sleep(3)
            os.system("cls")
            chinese()
        else:
            print("輸入不對哦 ~ ~ ~　\n重新輸入: ", end='')


def rank_list(stars, abc):  # 歌曲評價等級排行
    if (stars == 1):
        list_1.append(abc)
    elif (stars == 2):
        list_2.append(abc)
    elif (stars == 3):
        list_3.append(abc)
    elif (stars == 4):
        list_4.append(abc)
    elif (stars == 5):
        list_5.append(abc)


def chinese():  # 搜尋歌曲
    print('\n')
    print("你想搜尋哪首歌曲?")
    print("歌名: ", end='')  # 輸入歌曲名
    while True:
        str1 = str(input())
        if (str1 == ''):
            print("不能輸入空白哦 ! ! !")
            print("重新輸入: ", end='')
        else:
            break
    add = -1  # 代表歌曲還不確定有沒有在清單內
    for abc in chinese_dic:
        if (abc == str1):
            print("歌曲種類: " + chinese_dic[abc])
            # lyric(abc)
            evaluation(abc)
            add = 1  # 代表歌曲已在清單內
            break
    if (add != 1):
        kind(str1)


def evaluation(abc):  # 歌曲評價
    while True:
        print('\n')
        print("是否加入收藏並給予評價(是 / 否): ", end='')
        quest = str(input())  # 是否加入收藏
        if (quest == "是"):
            time.sleep(0.5)
            print("已成功加入收藏 ! ! !")
            print("給予歌曲評價 1 ★ ~ 5 ★.★.★.★.★ (1 ~ 5): ", end='')
            while True:
                stars = int(input())
                if (stars < 1 or stars > 5):
                    print("輸入不對哦 ~ ~ ~　\n重新輸入: ", end='')
                while (stars >= 1 and stars <= 5):
                    rank_list(stars, abc)
                    print("是否顯示自己對於所有收藏歌曲的評價排行(是 / 否): ", end='')
                    ans = str(input())
                    if (ans == "是"):
                        print("\n. . . 即將為你顯示出清單", end='')
                        for t in range(3):
                            print(" . ", end='')
                            time.sleep(1)
                        os.system("cls")
                        for num in range(6):
                            evaluation_list(num)
                        again()
                        break
                    elif (ans == "否"):
                        print("即將結束歌曲收藏功能 ! ! !")
                        os.system("cls")
                        again()
                        break
                    else:
                        print("輸入不對哦 ~ ~ ~　\n重新輸入: ", end='')
                        continue

        elif (quest == "否"):
            again()
            break
        else:
            print("輸入不對哦 ~ ~ ~　\n重新輸入: ", end='')
            continue


def evaluation_list(num):  # 顯示收藏歌曲排行
    print('\n')
    if (num == 1):
        print('★ : ', end='')
        print(list_1)
        print('\n')
    elif (num == 2):
        print('★.★ : ', end='')
        print(list_2)
        print('\n')
    elif (num == 3):
        print('★.★.★ : ', end='')
        print(list_3)
        print('\n')
    elif (num == 4):
        print('★.★.★.★ : ', end='')
        print(list_4)
        print('\n')
    elif (num == 5):
        print('★.★.★.★.★ : ', end='')
        print(list_5)
        print('\n')


def lyric(name):  # 歌曲歌詞
    print("\n. . . 即將為你顯示出歌詞", end='')
    for t in range(3):
        print(" . ", end='')
        time.sleep(1)
    os.system("cls")
    f = open('F:/歌庫/' + name + '.txt', 'r')
    # 這裡有點難搞，
    # 我們可能到時候報告的時候要準備一個隨身碟
    # 裡面存所有歌詞
    print(f.read())
    f.close()


def again():  # 是否結束程式
    print('\n')
    print("是否要結束? (是 / 否): ", end='')
    ans1 = str(input())
    if (ans1 == '否'):
        os.system("cls")
        while True:
            print("要列出目前清單還是繼續搜尋歌曲?(列出清單 / 搜尋歌曲): ", end='')
            ansr = str(input())
            if ansr == '列出清單':
                for num in range(6):
                    evaluation_list(num)
                again()
                break
            elif ansr == '搜尋歌曲':
                print("你還想聽哪種語言的歌曲 (中文 / 英文): ", end='')
                while True:
                    choose = str(input())
                    if (choose == "中文"):
                        chinese()
                    elif (choose == "英文"):
                        English()
                    else:
                        print("輸入不對哦 ~ ~ ~　\n重新輸入: ", end='')
                        continue
                    break
            else:
                print("Wrong Input!\n")

    elif (ans1 == '是'):
        print("~ ~ ~ 謝謝光臨 ~ ~ ~  ")


language = ["中文", "英文"]
print("歌曲語言 : 中文 / 英文")
while True:
    print("選擇語言: ", end='')
    l = str(input())
    if(l == language[0]):
        print('\n')
        print("""此程式目的為創造出私人歌庫 ! ! !""")
        chinese()
    elif(l == language[1]):
        print("\nBuild Your Own Playlist Easily Using This App!\n")
        English()
    else:
        print("輸入不對哦 ~ ~ ~")
        continue
    break
