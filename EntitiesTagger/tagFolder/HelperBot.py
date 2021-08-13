import pyperclip

list1 = []
list2 = []
count = 0
while True:
    print("-----------------------")
    s = input()
    list1.append(s)
    listz = []
    for i in s.split():
        listz.append("o")
    result = str(listz).replace("\'","\"")
    print(result)
    pyperclip.copy(result)
    final = input()
    list2.append(final)
    count+=1
    print(count)
    print(str(list1).lstrip("[").rstrip("]").replace("\'","\""))
    print(str(list2)[1:-1].replace("\'",""))
