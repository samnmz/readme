name = 'saman'
last_name = 'namazzadeh'
age = '18'

all = name + " " + last_name + " " + age
all2 = "hi my name is %s and my last name is %s and im %s years old" % (name, last_name, age)
all3 = 'hi my name is {}, my lastname is {} and im {} years old'.format(name, last_name, age)

name2 = all3.split()

list = ['saman', 'ali', 'amir', 'sobhan', 17, 18, 'new']
#print(list.count(18))

a = list.append('abbas')
#print(list)

a1 = list.extend('khiyar')
#print(list)

a2 = list.insert(598, 33)
#print(list)

number = [1 , 2, 3, 4, 5, 6, 17]
a3 = number.remove(17)
a3 = number.append(55)


dic = {'name': 'saman', 'lastname': 'namazzadeh', 'age': 17}
#print(dic['name'])

nomarat = {
    'saman': 
    {
        'lastname': 'nmz',
        'varzesh': 20,
        'adabiat': 10,
    },
    'amir': 
    {
        'lastname': 'enzva',
        'varzesh': 20,
        'adabiat': 14,
    }
}

#print(nomarat)

names = {'tehran': 'azadi', 'paris': 'ifel'}
new = names['tehran'] = 'milad'
#print(new)

prices = {
    'apple': 1500,
    'banana': 1000,
    'orange': 1200,
}
a = prices['banana'] = 1100
#a = prices.pop('apple')
del prices['apple']
#print(prices)

number = (1, 2, 3, 4, 5)
#print(number[0])

coordinate = (3, 4)
origin = (0, 0)
distance = ((coordinate[0] - origin[0]) ** 2 + (coordinate[1] - origin[1]) ** 2)
#print(distance)


my_set = {1, 2, 2, 3, 4, 5, 5, 6}
b = my_set.add(33)
#print(my_set)


setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
i = setA.intersection(setB)
#print(i)
u = setA.union(setB)
#print(u)



x = 5
#print(3< x <= 7)


#a = int(input('enter a number '))
#b = int(input('enter a number '))
#c = int(input('enter a number '))

#if a < b <= c:
    #print('True')
#else:
    #print('False')

# price = int(input('enter the price of the shol '))
#if price > 50000:
    #takhfif = price * 20 / 100
    #print(takhfif)
#elif price >= 20000 and price <= 50000:
    #takhfif = price * 10 / 100
    #print(takhfif)
#else:  
    #print('takhfif vojod nadarad')


people = {
    'jadi': (20, 170),
    'saman': (60, 185),
    'amir': (85, 188)
}
#for item in people:
    #print(item, people[item][1])
    #print(f'hi my name is {key}, and i have {item}')


# my_tupple = (1, 4, 'mive', 'abbas')
# for i in my_tupple:
#     print(i)

#for i in range(1, 4):
   # print(i * 2)


words = ['Python', 'is', 'awesome']
result = ''

for words in words:
    result += words[0]

#print(result)


# x = 1
# while x < 5:
#     x += 1
# print(x)


# inpt = int(input('enter a number '))
# nesf = 0

# while nesf != 1:
#     if inpt % 2 == 0:
#         nesf = inpt / 2
        
#     if nesf % 2 != 0:
#         nesf = nesf * 3 + 1
#         continue
#     print(nesf)
   
        
        
#     if nesf != 1:
#         continue
#     else:
#         break
    



adad = int(input('enter the number: '))
if adad % 3 == 0 and adad % 5 == 0:
    print("افسانه ای")
elif adad % 3 == 0:
    print("جادویی")
elif adad % 5 == 0:
    print("نفرین شده")
else:
    print("معمولی")