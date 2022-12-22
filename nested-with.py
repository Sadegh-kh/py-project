with open("note.txt", "r") as file, open("note2.txt") as file2, open("new.txt", "w+") as file3:
    for line in file:
        file3.write(line)
    file3.write("\n")
    for line in file2:
        file3.write(line)
    file3.seek(0)
    for line in file3:
        print(line)
