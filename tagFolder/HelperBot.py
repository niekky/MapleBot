count = 0
while True:
    s = input()
    listz = []
    for i in s.split():
        listz.append("o")
    print(str(listz).replace("\'","\""))
    count+=1
    print(count)
