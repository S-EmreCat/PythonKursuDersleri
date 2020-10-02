

with open("newfile.txt", "r+", encoding="utf-8") as file:
    file.seek(15)
    file.write("deneme")

with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())