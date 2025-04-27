import glob

def CreatePage():
    page_title = input("Enter Name Of New Note Page:  ").upper()
    page = open(f"{page_title}.txt","w")
    page.close()
    print(f"New File '{page_title}' created!\n")

def ListNotes():
    for i in glob.glob("*.txt"):
        print(i)

def EditFiles(file_name):
    test = glob.glob("*.txt")
    file_name = str(file_name) + ".txt"
    file_edit = ""
    file_choice = ""
    file_read = "r"
    file_append = "a"
    working = True
    
    while working:
        if file_name not in test:
            print("Sorry file does not exist!\n")
            file_name = input("Enter Name Of File:  ").upper() + ".txt"
        else:
            print(f"Accessing File '{file_name}'!\n")
            working = False
    
    file_choice = input("To Read The File Enter 'R'/To Add to file enter 'A':\n").lower()
    if file_choice == "a":
        file_edit = open(f"{file_name}", "a")
        file_append = input("Enter What You Wish To add To THe file:\n")
        file_edit.write(f"\n{file_append}")
        file_edit.close()

EditFiles("TEST NOTE")
#Finishing The EditFiles function