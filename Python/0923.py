import calendar
print(calendar.month(2010,10))
tax = 1931 // 12  #// vs /
print(tax)
print('apple', 'orange', 'lemon')
print(11 > 10)
ch = "生日快樂 \n"
en = "happy, birthday"
print(ch ,en)
s1= '''sunday monday tuesday
''' *2
print(s1)
test = 'hello'
print(test.upper())  #lower
word = 'benchen'
print(word.count('e'))

#串列型別
string1 = ['benchen', 'is']
string1.append('smart')
print(string1)

#字典型別
activity = {'1':'PE Class', '2':'programming', '3':'tw'}
print(activity['1'])
print(activity.keys())
print(activity.values())

#序對型別
sample = ('sdasd', '546', 'dasd')
print(sample)

listsport = ['Mon: 籃球', 'Tue: 羽球', 'Wed: 羽球', 'Thu: 排球', 'Fri: 排球', 'Sat: 健身', 'Sun: 健身']
print('一三五做什麼:', listsport[0:5:2])
print('二四六做什麼:', listsport[1:6:2])
print('周末做什麼:', listsport[5:])
print('禮拜五以前做了:', listsport[:6])
print('禮拜三以後做了', listsport[3:])