f=open("C:/Users/skarn/Documents/GitHub/Python/Test.txt", 'r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close()