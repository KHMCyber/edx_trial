myFile = open("firstFile.txt", "w")
myFile.write('Bismillah-ir-Rahman-ir-Raheem \n')
myFile.write('Alhumdu lillahi Rub-il-aalameen')
myFile.close()

myFile = open('firstFile.txt', 'r')
print('reading thru .read()\n')
print(myFile.read())
myFile.close()

myFile = open('firstFile.txt', 'r')
print('reading thru .readline()\n')
print(myFile.readline())
myFile.close()

myFile = open('firstFile.txt', 'r')
print('reading thru readline(100)\n')
print(myFile.readline(100))
myFile.close()

myFile = open('firstFile.txt', 'r')
print('reading thru for loop\n')
i = 0
for line in myFile:
    print('reading line-%i' % i)
    print(myFile.readline())
    i += 1
