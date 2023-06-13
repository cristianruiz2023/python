'''larguest_so_far =-1

print("Before",larguest_so_far )

for the_num in [9,41,12,3,74,15]:
    if the_num > larguest_so_far:
        larguest_so_far=the_num
    print(larguest_so_far,the_num)
print("after",larguest_so_far)

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

zork = 0
print('before',zork)

for thing in [9,41,12,3,74,15]:
    zork = zork +1
    print(zork,thing)
print('after', thing)

zork = 0
print('before',zork)

print('**************************')

for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork,thing)
print('after', thing)

print('************************************')

count = 0
sum = 0
print('before',count,sum)
for value in [9,41,12,3,74,15]:
    count+=1
    sum=sum+value
    print(count,sum,value)
print('after',count,sum,sum/value)

print('********************************************')

print('before')

for value in [9,41,12,3,74,15]:
    if value >20 :
        print('large number',value)
print('after')

print('*****************************************************')

found = False
print('before',found)
for value in [9,41,12,3,74,15]:
    if value ==3:
        found = True
    print(found,value)
print('after',found)

print('*****************************************************')

small_so_far =99

print("Before",small_so_far )

for the_num in [9,41,12,3,74,15]:
    if the_num < small_so_far:
        small_so_far=the_num
    print(small_so_far,the_num)
print("after",small_so_far)'''

print('*****************************************************')

smallest = None
print('before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest,value)
print('after',smallest)


