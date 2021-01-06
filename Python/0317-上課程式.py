#2020.03.17

print(34 + 56) #整數
number = 55

print(5 + 3.4) # = 8.4 浮點數(小數
print(5 / 2)

complex = 5 + 5j #複數
print(complex + (3 + 1j) )

message = "生日快樂!"
message = '生日快樂!'

print('this is "a"')

print('thunder' + 'bolt')
print('hunter' * 2)

text = 'hello'
print(text.upper())
print(text.count('l'))

#[57, 'apple', 'banana'] #串列List
Agroup = ['kazu', 'gorou']
Agroup.append('dai') #增加元素
print(Agroup)
Agroup.remove('kazu') #移除元素
print(Agroup)
Agroup.sort() #排序(字串根據ASCII排序)
print(Agroup)

#test = [57, 'apple', 'banana'] #list內同時有字串、數字不可排序
#print(Agroup)
#test.sort()
#>>>TypeError: '<' not supported between instances of 'str' and 'int'
