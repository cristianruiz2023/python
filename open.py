



fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1

print('cantidad de lineas: ',count)

fhand = open('mbox-short.txt')
inp=fhand.read()
print(len(inp))
print(inp[:20])

fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)
print('***********************************')

fhand = open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith('From:'):
        print(line)

print('************************************')

fhand = open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)