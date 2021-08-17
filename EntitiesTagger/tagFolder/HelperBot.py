import pyperclip

count = 0
this_list = []
while True:
    o_list = []
    sentence = input("Your sentence below : \n")
    for letter in sentence.split():
        o_list.append("o")
        pyperclip.copy(str(o_list))
    print("Paste and edit below : ")
    tag = input()
    final = {"sentence": sentence,
    "tag": tag}
    this_list.append(final)
    print("--------------------------")
    print(str(this_list)[1:-1].replace("\"","").replace("\'","\""))
    print("--------------------------")
    count += 1
    print("Total : ",count)