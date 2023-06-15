
fruit = 'banana'
print(len(fruit))

print('*************************')

fruit = 'banana'
x = len(fruit)
print(x)

print('*************************')
#enumera los indices con su respectivo char con bucle while
fruit = 'Banana'
index = 0

while index < len(fruit):
    leter = fruit[index]
    print(index,leter)
    index +=1

print('*************************')
print('ciclo for')

fruit='Banana'
for letter in fruit:
    print(letter)


print('*************************')
#conteo de caracteres con ciclo for
word ='Banana'
count = 0

for letter in word:
    if letter == 'a':
        count +=1
print(count)

print('*************************')
# M o n t y   P y t h o  n
# 0 1 2 3 4 5 6 7 8 9 10 11

s= 'Monty Python'

print(s[:2])#Mo
print(s[8:])#thon
print(s[:])#Monty Python


print('*************************')


fruit = 'banana'
'n' in fruit
#True
'm' in fruit
#false
'nan' in fruit
#True
if 'a' in fruit:
    print('Found it')
#'found it'

print('*************************')

if word =='banana':
    print('All right, banana')
if word < 'banana':
    print('you word '+word+'comes before banana')
elif word > 'banana':
    print('you word'+word+'comes after banana')
else:
    print('All right bananas')

print('*************************')
#.find()

fruit ='banana'
pos=fruit.find('na')
print(pos)
#2 se encuentra en la pos 2
aa=fruit.find('z')
print(aa)
#-1 no contiene lo que se busca

print('*************************')
#upper

great='Hello Bob'
nnn=great.upper()
print(nnn)
#'HELLO BOB'
www=great.lower()
print(www)
#hello bob

print('*************************')
#replace()

great='Hello Bob'
nstr=great.replace('Bob','Jane')
print(nstr)# 'Hello Jane'

ztr=great.replace('o','x')
print(ztr)# Hellx Bxb

print('*************************')
#strip
great ='    Hello Bob   '
great.strip()
#'Hello Bob'

print('*************************')
#startswith

line='Please have a nice day'
line.startswith('Please')
#True
line.startswith('p')
#False

print('*************************')
#convinados

data='From stephen.marresh@utc.ac.za Sat Jan 5 09:14:12 2008'

atpos=data.find('@')
print(atpos)
#20
sppos=data.find(' ',atpos)
print(sppos)
#30
host=data[atpos+1 : sppos]
print(host)
#utc.ac.za
