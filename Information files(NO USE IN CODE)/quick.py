f = open('data/playerData.py','r')
for line in f:
    if line != '\n':
        print(line)
f.close()
