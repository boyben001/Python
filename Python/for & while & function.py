#for ---------
for count in range(4):
    print('重複執行')
    print(count)
print('\n')
music_list = ['death metal', 'rock', 'anime', 'pop']
for music in music_list:    #list type
    print('now playing : ' + music)
print('\n')
menu = {'拉麵':500, '炒飯':430, '煎餃':210}
for order in menu:
    print(order)
    print(menu[order] * 1.08)  #dictionary type
print('\n')

family = ['大明', '大名', '小明']
for kid in family:
    print('Good Morning ! , ' + kid)
    print('Wake Up')
    print("Have a breakfast")
    continue
    print('Leave for school')
print('\n')
#while -------

counter = 0
while(counter < 5):
    print(counter)
    counter = counter + 1
print('\n')
while(True):
    print('揮拳')
    print('星爆氣流斬')
    break
print('\n')

#function by myself--------
def washingmachine(mode):
    print('注水')
    if (mode == 'soft'):
        print('輕柔清洗')
    elif (mode == 'hard'):
        print('強力清洗')
    else:
        print('一般清洗')
mode = 'soft'
washingmachine(mode)
print('\n')
def area(radius):
    result = radius * radius * 3.14
    return result
radius = 2
print(area(radius))
print('\n')

#function by python
print(len('thunderbolt'))
animal = ['cat', 'dog', 'pig']
print(len(animal))

print(max(100, 101, 99))
print(min(100, 101, 99))

print(max('thunderbolt'))   #according to ASCII Code
print(min('1Aa'))  
print(max('1Aa'))

print(sorted([80, 99, 100, 101, 81]))