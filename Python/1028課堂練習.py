#利用飲食紅黃綠圖片設計以下2項應用
#利用List分別建立不同燈號的食物項目並利用迴圈印出(至少5樣)
#利用Dict分別建立不同燈號得食物項目及熱量(google或自己假設)，
# 逐一印出並設計計算熱量的函式來顯示不同燈號的熱量總和......
# (sorted()可以排序數字大小)
calories = ['spaghetti', 'cookies', 'cake', 'pizza', 'cereal']
food = {'spaghetti':1000, 'cookies':500, 'cake':1200, 'pizza':1300, 'cereal':300}
def choose(lunch):
    if (lunch == 'spaghetti'):
        print(str(food['spaghetti']) + ' calories')
        light(food['spaghetti'])
    elif (lunch == 'cookies'):
        print(str(food['cookies']) + ' calories')
        light(food['cookies'])
    elif (lunch == 'cake'):
        print(str(food['cake']) + ' calories')
        light(food['cake'])
    elif (lunch == 'pizza'):
        print(str(food['pizza']) + ' calories')
        light(food['pizza'])
    elif (lunch == 'cereal'):
        print(str(food['cereal']) + ' calories')
        light(food['cereal'])
def light(num):
    if (num >= 1000):
        print('It is a red light food, do not eat!')
    elif (num >= 500 and num < 1000):
        print('It is a yellow light food, please not to have too much!')
    else:
        print('It is a green light food, you can have as many as possible')
    return
def bmr():
    male_result = 5 + (13.7 * weight) + (5 * height) - (6.8 * age)
    female_result = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    if (gender == 'male'):
        return male_result
    elif (gender == 'female'):
        return female_result
print('Enter your age: ')
age = int(input())
print('your weight(kg): ')
weight = float(input())
print('your height(cm): ')
height = float(input())
print('your gender(male/female): ')
gender = str(input())
print('You can consume ' + str(bmr()) + ' calories in today')
print('what do you want to eat for lunch?')
for lunch in calories:
    print(lunch)
print('Enter the food you want below: ')
ch = input()
choose(ch)
for order in food:
    if (ch == order):
        has = food[order]
left = int((bmr()) - int(has))
print('So you only have ' + str(int((bmr()) - int(has))) + ' calories left in today!!!')