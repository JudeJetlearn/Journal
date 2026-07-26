journal = r"C:\Users\judea\OneDrive\Desktop\Python V2\Class4\Journal.txt"

while True:

    print("1) View File ")
    print("2) Add to File ")
    print("3) Remove Info on File ")

    option = int(input("Pick An Option. "))

    if option == 1 :
        with open(journal,"r")as readFile :
            txt = readFile.read()
            print(txt)

    if option == 2 :
        with open(journal,"a")as writeFile :
            text = input("Type the Info to Add. ")
            writeFile.write("\n"+text)
    
    if option == 3 :
        indexRemove = int(input("Enter the LINE NUMBER you want to remove. ")) - 1
        with open(journal,"r")as removeFile :
            lines = removeFile.readlines()
            lines.pop(indexRemove)
            print(lines)

        with open(journal,"w")as writeMode:
            for i in lines:
                writeMode.write(i)





    